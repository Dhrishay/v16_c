import os
import requests
from odoo.addons.OCC.Core.STEPControl import STEPControl_Reader
from odoo.addons.OCC.Core.Bnd import Bnd_Box
from odoo.addons.OCC.Core.TopoDS import TopoDS_Shape, TopoDS_Vertex
from odoo.addons.OCC.Core.gp import gp_Pnt
from odoo.addons.OCC.Core.TopExp import TopExp_Explorer
from odoo.addons.OCC.Core.TopAbs import TopAbs_VERTEX
from odoo.addons.OCC.Core.BRep import BRep_Tool
from urllib.parse import urlparse
from odoo.http import request, route
from odoo import http
import json
import tempfile


import logging
_logger = logging.getLogger(__name__)
class PowerVisController(http.Controller):

    # Function to sanitize the file name from the URL
    def sanitize_filename(self, url):
        # Parse the URL to get the filename and remove any query parameters
        parsed_url = urlparse(url)
        file_name = os.path.basename(parsed_url.path)

        # Optionally, sanitize the file name (e.g., remove any special characters)
        file_name = file_name.replace("?", "_").replace("&", "_")

        return file_name

    # Function to process the STEP file and get bounding box
    def analyzestep(self, file_path):
        step_reader = STEPControl_Reader()
        status = step_reader.ReadFile(file_path)

        if status != 1:  # 1 means success
            raise Exception("Error reading the STEP file ")

        step_reader.TransferRoots()
        shape = step_reader.OneShape()

        # Create a bounding box for the shape
        bounding_box = Bnd_Box()

        # Use TopExp_Explorer to traverse the shape and get the vertices
        explorer = TopExp_Explorer(shape, TopAbs_VERTEX)

        while explorer.More():
            vertex = explorer.Current()

            # Extract the point from the vertex using BRep_Tool.Pnt()
            point = BRep_Tool.Pnt(vertex)

            # Add the point to the bounding box
            bounding_box.Add(point)
            explorer.Next()

        # Get the min and max values of the bounding box
        x_min, y_min, z_min, x_max, y_max, z_max = bounding_box.Get()

        # Calculate dimensions and volume
        length = x_max - x_min
        width = y_max - y_min
        height = z_max - z_min
        volume = length * width * height  # Simple volume calculation (assuming rectangular box)

        return length, width, height, volume, "mm"  # Returning 'mm' as unit (millimeters)

    # API endpoint to process the STEP file
    @http.route('/api/analyze', methods=['POST'], type='json', auth="public", website=True, csrf=False)
    def process_step_file(self, **kw):
        data = request.httprequest.data
        data = json.loads(data.decode('utf-8'))
        file_url = data.get('file_url')
        if not file_url:
            return ({"error": "No file URL provided"})
        try:
            # Sanitize the file name from the URL
            file_name = self.sanitize_filename(file_url)
            directory = tempfile.mkdtemp()
            local_file_path = os.path.join(directory, file_name)
            # Download the STEP file
            response = requests.get(file_url)
            with open(local_file_path, 'wb') as file:
                file.write(response.content)
            # Process the downloaded file and get bounding box
            length, width, height, volume, unit = self.analyzestep(local_file_path)
            # Return the result as a JSON response
            return ({
                "length": length,
                "width": width,
                "height": height,
                "volume": volume / 1000,
                "unit": unit  # Adding the unit (e.g., "mm" for millimeters)
            })

        except Exception as e:
            return ({"error": str(e)})

