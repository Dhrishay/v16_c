/** @odoo-module **/

import ajax from 'web.ajax';
import {
    session
} from "@web/session";

let selectedFile = null;

$(document).ready(function() {

    if($('.message-item').length > 0){
        if ($(window).width() > 768) {
            setTimeout(function(){
                $($('.message-item')[0]).click();
            }, 0); // Added timeout delay for proper execution
        }
    }

    $('#attachment-input').on('change', function (event) {
        selectedFile = event.target.files[0];

        if (selectedFile) {
            $('.file-card .file-name').text(selectedFile.name);

            $('.file-card').removeClass('d-none');
        }
    });

    $('.back-img').on('click', function () {
        $('.message-list').removeClass('d-none');
        $('.message-detail').attr('style', 'display: done !important');
    });

    // Event listener for the "link-button" to open the file dialog
    $('.link-button').on('click', function () {
        $('#attachment-input').click();
    });

    $('.close-message').on('click', function(ev) {
        $(this.parentElement.parentElement.parentElement).addClass('d-none')
    })

    $('.remove-file').on('click', function(ev) {
        // Clear the file input
        $('#attachment-input').val('');

        // Hide the file-card
        $('.file-card').addClass('d-none');

        // Optionally clear the file name display
        $('.file-name').text('');
    })

    $('.message-item-portal').on('click', function() {
        if($(this).hasClass('send_quey_btn')){
            $($(this).siblings()).removeClass('d-none');
        }
        else{
            $('.message-item-portal').each(function() {
                if(!$($(this).parent().siblings()[1]).hasClass('d-none')){
                    $($(this).parent().siblings()[1]).addClass('d-none')
                }
            });
            $($(this).parent().siblings()).removeClass('d-none');
        }
        const resModel = $(this).data('res-model');
        const resId = $(this).data('res-id');
        const userId = $(this).data('user-id'); // Get the user_id from the data attribute
        const categ = $($(this).parent().parent()).find('.category').text();
        const msgId = $($(this).parent().parent()).find('.message-id').text();
        fetchMessageDetails(resModel, resId, userId, categ, msgId);

    });

    $('.send-message-btn').on('click', function(){
        $('.message-item-portal').click();
    })

    $('.message-item').on('click', function() {
        $('.message-item').removeClass('active');
        $(this).addClass('active');

        const resModel = $(this).data('res-model');
        const resId = $(this).data('res-id');
        const userId = $(this).data('user-id'); // Get the user_id from the data attribute
        const categ = $(this).find('.category').text();
        const msgId = $(this).find('.message-id').text();

        // Check if '.message-detail' has styling 'display: none'
        const messageDetail = $('.message-detail');
        if (messageDetail.css('display') === 'none') {
            // Add 'd-none' class to parent elements
            messageDetail.attr('style', 'display: flex !important');
            $(this).parent().parent().addClass('d-none');
        }

        console.log("Clicked on message with user_id: ", userId);

        fetchMessageDetails(resModel, resId, userId, categ, msgId);
    });

    $('.send-button').on('click', async function() {
        const messageInput = $(this).closest('.message-input').find('input');
        const messageText = messageInput.val().trim();

        const resModel = $('.message-detail').attr('data-res-model');
        const resId = $('.message-detail').attr('data-res-id');
        $('.file-card').addClass('d-none');
        let attachmentId = null;
        if (!messageText) {
            alert('Message cannot be empty!');
            return;
        }

        const fileInput = $('#attachment-input')[0];
        const file = fileInput.files[0];
        
        if (file) {
            const formData = new FormData();
            formData.append('file', file);
            formData.append('res_model', resModel);
            formData.append('res_id', resId);

            const uploadResponse = await $.ajax({
                url: '/custom/attachment/create',
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
            });

            attachmentId = uploadResponse; // Capture the attachment ID from the response
        }

        const params = {
            res_model: resModel,
            res_id: resId,
            message: messageText
        };

        if (attachmentId) {
            // If attachmentId is available, include it in params
            params.attachment_ids = [attachmentId.id];
            params.attachment_tokens = [attachmentId.access_token];
        } 

        try {
            // Send the message via AJAX
            const result = await ajax.jsonRpc('/mail/chatter_post', 'call', params);

            // Trigger a click event on the corresponding `.message-item` to refresh details
            const matchingItem = $(`.message-item[data-res-model="${resModel}"][data-res-id="${resId}"]`);
            matchingItem.find('.msg-preview').text(messageText)
            if (matchingItem.length) {
                matchingItem.trigger('click', { messageText: messageText });
            } else {
                console.warn('No matching message-item found for resModel and resId.');
            }

            // Clear the input field
            messageInput.val('');
        } catch (error) {
            console.error('Error posting the message:', error);
        }
    });

    $('.send-button-portal').on('click', async function() {
        const messageInput = $(this).closest('.message-input').find('input');
        const messageText = messageInput.val().trim();

        const resModel = $(this).parent().parent().parent().attr('data-res-model');
        const resId = $(this).parent().parent().parent().attr('data-res-id');
        $('.file-card').addClass('d-none');
        let attachmentId = null;
        if (!messageText) {
            alert('Message cannot be empty!');
            return;
        }

        const fileInput = $('#attachment-input')[0];
        const file = fileInput.files[0];

        if (file) {
            const formData = new FormData();
            formData.append('file', file);
            formData.append('res_model', resModel);
            formData.append('res_id', resId);

            const uploadResponse = await $.ajax({
                url: '/custom/attachment/create',
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
            });

            attachmentId = uploadResponse; // Capture the attachment ID from the response
        }

        const params = {
            res_model: resModel,
            res_id: resId,
            message: messageText
        };

        if (attachmentId) {
            // If attachmentId is available, include it in params
            params.attachment_ids = [attachmentId.id];
            params.attachment_tokens = [attachmentId.access_token];
        }

        try {
            // Send the message via AJAX
            const result = await ajax.jsonRpc('/mail/chatter_post', 'call', params);

            // Clear the input field
            messageInput.val('');
        } catch (error) {
            console.error('Error posting the message:', error);
        }
        $(this.parentElement.parentElement.parentElement.parentElement).find('.message-item-portal').click();
        var chatContent = $(this.parentElement.parentElement.parentElement).find('.chat-content');
        chatContent.scrollTop(chatContent[0].scrollHeight);
    });
    if ($('.search_text').length){
        setTimeout(() => {
                $('.search_text').attr('placeholder', 'Search')
        }, 500);
    }
});

// Fetch message details from the server
async function fetchMessageDetails(resModel, resId, userId, categ, msgId) {
    try {
        const params = {
            res_model: resModel,
            res_id: resId,
            domain: false,
            limit: 10,
            offset: 0,
        };

        const result = await ajax.jsonRpc('/mail/chatter_fetch', 'call', params);

        const messages = preprocessMessages(result.messages);
        const messageCount = result.message_count;

        updateMessageDetail(messages, userId, categ, msgId, resModel, resId);
        updateMessageCount(messageCount);

    } catch (error) {
        console.error('Error fetching message details:', error);
    }
}

// Preprocess messages (if needed)
function preprocessMessages(messages) {
    return messages;
}

// Update the message detail container with fetched messages
function updateMessageDetail(messages, userId, categ, msgId, resModel, resId) {
    if($('.message-details').length == 0){
        const messageDetailContainer = $('.message-detail');

        messageDetailContainer.find('.chat-content').empty(); // Clear existing messages
        messageDetailContainer.attr('data-res-model', resModel);
        messageDetailContainer.attr('data-res-id', resId);

        if (messages.length > 0) {
            messages.reverse();
            messages.forEach((message) => {
                const messageHtml = `
                    <div class="chat-message ${message.author.id === userId ? 'outgoing' : 'incoming'}">
                        <div class="user-img">
                            <img src="/web/image/res.partner/${message.author.id}/avatar_128"/>
                        </div>
                        <div class="msg-details">
                            <div class="sender">${message.author.id === userId ? 'You' : message.author.name} * ${message.date.split(' ')[0]}</div>
                            <p>${$('<div>').html(message.body).text().trim().replace(/\n/g, '<br/>')}</p>
                            ${
                                message.attachment_ids && message.attachment_ids.length
                                    ? message.attachment_ids.map(attachment => `
                                        <div class="file-card">
                                            <div class="file-card-content">
                                                <span class="file-icon">
                                                    <img src="/cr_web_portal/static/src/images/mech-custom/link.png"/>
                                                </span>
                                                <span class="file-name">${attachment.name}</span>
                                                <a href="/web/content/${attachment.id}?download=true&access_token=${attachment.access_token}" target="_blank" class="download-btn">
                                                    <img src="/cr_web_portal/static/src/images/mech-custom/import.png"/>
                                                </a>
                                            </div>
                                        </div>
                                    `).join('')
                                    : ''
                            }
                        </div>
                    </div>
                `;

                messageDetailContainer.find('.chat-content').append(messageHtml);
            });
            var chatContent = messageDetailContainer.find('.chat-content');
            chatContent.scrollTop(chatContent[0].scrollHeight);
        } else {
            messageDetailContainer.find('.chat-content').append('<p style="text-align: center;">No messages available</p>');
        }
        messageDetailContainer.find('.helpdesk-button').removeClass('d-none');
        if (categ == "Sales Order"){
            let orderUrl = "/my/orders/" + resId;
            messageDetailContainer.find('.helpdesk-button').attr("href", orderUrl);
        }
        else if (categ == "Inquiries"){
            let orderUrl = "/my/inquiry/quotes/" + resId;
            messageDetailContainer.find('.helpdesk-button').attr("href", orderUrl);
        }
        else if (categ == "Invoices & Bills"){
            let orderUrl = "/my/invoices/" + resId;
            messageDetailContainer.find('.helpdesk-button').attr("href", orderUrl);
        }
        else if (categ == "Quotation"){
            let orderUrl = "/my/orders/" + resId;
            messageDetailContainer.find('.helpdesk-button').attr("href", orderUrl);
        }
        else if (categ == "Ticket"){
            let orderUrl = "";
            messageDetailContainer.find('.helpdesk-button').attr("href", orderUrl);
            messageDetailContainer.find('.helpdesk-button').addClass('d-none');
        }
        // Update metadata
        messageDetailContainer.find('.message-id').text(msgId);
        messageDetailContainer.find('.category').text(categ);
    }
    else{
        $('.message-details').each(function () {
            var $this = $(this);
            var model = $this.attr('data-res-model');
            var id = $this.attr('data-res-id');

            // Check if the model and ID match
            if (model === resModel && id === String(resId)) {
                const messageDetailContainer = $(this);
                messageDetailContainer.find('.chat-content').empty(); // Clear existing messages
                messageDetailContainer.attr('data-res-model', resModel);
                messageDetailContainer.attr('data-res-id', resId);

                if (messages.length > 0) {
                    messages.reverse();
                    messages.forEach((message) => {
                        const messageHtml = `
                            <div class="chat-message ${message.author.id === userId ? 'outgoing' : 'incoming'}">
                                <div class="user-img">
                                    <img src="/web/image/res.partner/${message.author.id}/avatar_128"/>
                                </div>
                                <div class="msg-details">
                                    <div class="sender">${message.author.id === userId ? 'You' : message.author.name} * ${message.date.split(' ')[0]}</div>
                                    <p>${$('<div>').html(message.body).text().trim().replace(/\n/g, '<br/>')}</p>
                                    ${
                                        message.attachment_ids && message.attachment_ids.length
                                            ? message.attachment_ids.map(attachment => `
                                                <div class="file-card">
                                                    <div class="file-card-content">
                                                        <span class="file-icon">
                                                            <img src="/cr_web_portal/static/src/images/mech-custom/link.png"/>
                                                        </span>
                                                        <span class="file-name">${attachment.name}</span>
                                                        <a href="/web/content/${attachment.id}?download=true&access_token=${attachment.access_token}" target="_blank" class="download-btn">
                                                            <img src="/cr_web_portal/static/src/images/mech-custom/import.png"/>
                                                        </a>
                                                    </div>
                                                </div>
                                            `).join('')
                                            : ''
                                    }
                                </div>
                            </div>
                        `;

                        messageDetailContainer.find('.chat-content').append(messageHtml);
                    });
                    var chatContent = $(this.parentElement.parentElement.parentElement).find('.chat-content');
                    chatContent.scrollTop(chatContent[0].scrollHeight);
                } else {
                    messageDetailContainer.find('.chat-content').append('<p style="text-align: center;">No messages available</p>');
                }
                messageDetailContainer.find('.helpdesk-button').removeClass('d-none');
                if (categ == "Sales Order"){
                    let orderUrl = "/my/orders/" + resId;
                    messageDetailContainer.find('.helpdesk-button').attr("href", orderUrl);
                }
                else if (categ == "Inquiries"){
                    let orderUrl = "/my/inquiry/quotes/" + resId;
                    messageDetailContainer.find('.helpdesk-button').attr("href", orderUrl);
                }
                else if (categ == "Invoices & Bills"){
                    let orderUrl = "/my/invoices/" + resId;
                    messageDetailContainer.find('.helpdesk-button').attr("href", orderUrl);
                }
                else if (categ == "Quotation"){
                    let orderUrl = "/my/orders/" + resId;
                    messageDetailContainer.find('.helpdesk-button').attr("href", orderUrl);
                }
                else if (categ == "Ticket"){
                    let orderUrl = "";
                    messageDetailContainer.find('.helpdesk-button').attr("href", orderUrl);
                    messageDetailContainer.find('.helpdesk-button').addClass('d-none');
                }
            }
        })
    }
}

// Update the message count
function updateMessageCount(messageCount) {
    $('.message-count').text(`Total messages: ${messageCount}`);
}
