// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.ready(function() {

	if(frappe.utils.get_url_arg('subject')) {
	  $('[name="subject"]').val(frappe.utils.get_url_arg('subject'));
	}
	
	/*
	Contact Form: Basic
	*/
	$('.contact-form').each(function(){
		$(this).validate({
			submitHandler: function(form) {

				var $form = $(form),
					$messageSuccess = $form.find('.contact-form-success'),
					$messageError = $form.find('.contact-alert'),
					$submitButton = $(this.submitButton),
					$errorMessage = $form.find('.mail-error-message'),
					submitButtonText = $submitButton.val();

				$submitButton.val( $submitButton.data('loading-text') ? $submitButton.data('loading-text') : 'Loading...' ).attr('disabled', true);

				// Fields Data
				var formData = $form.serializeArray(),
					data = {};

				$(formData).each(function(index, obj){
				    data[obj.name] = obj.value;
				});
				
				frappe.send_message({
					subject: $('[name="subject"]').val(),
					sender: $('[name="email"]').val(),
					message: $('[name="message"]').val(),
					callback: function(r) {
						if(r.message==="okay") {
							$messageSuccess.removeClass('d-none');
							$messageError.addClass('d-none');

							// Reset Form
							$form.find('.form-control')
								.val('')
								.blur()
								.parent()
								.removeClass('has-success')
								.removeClass('has-danger')
								.find('label.error')
								.remove();

							if (($messageSuccess.offset().top - 80) < $(window).scrollTop()) {
								$('html, body').animate({
									scrollTop: $messageSuccess.offset().top - 80
								}, 300);
							}

							$form.find('.form-control').removeClass('error');

							$submitButton.val( submitButtonText ).attr('disabled', false);
							
							return;
							
						} else {
							$errorMessage.html(data.errorMessage).show();
							console.log(r.exc);
						}
						$messageError.removeClass('d-none');
						$messageSuccess.addClass('d-none');

						if (($messageError.offset().top - 80) < $(window).scrollTop()) {
							$('html, body').animate({
								scrollTop: $messageError.offset().top - 80
							}, 300);
						}

						$form.find('.has-success')
							.removeClass('has-success');
							
						$submitButton.val( submitButtonText ).attr('disabled', false);
					}
				}, this);
				return false;
			}
		});
	});
	

});


