// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.ready(function() {

	if(! $('[name="subject"]').val()) {
	  var item_code = $('[name="item-code"]').val();
	  $('[name="subject"]').val('Inquiry about ' + item_code);
	}
	if (!['Administrator', 'Guest'].includes(frappe.session.user)) {
			$('[name="email_id"]').val(frappe.session.user);
			$('[name="lead_name"]').val(frappe.get_cookie('full_name'));
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

				frappe.call({
					method: 'hendaza_custom_site.utils.create_lead_for_item_inquiry',
					args: {
						lead: $('[name="lead_name"]').val(),
						mobile: $('[name="mobile_no"]').val(),
						email: $('[name="email_id"]').val(),
						subject: $('[name="subject"]').val(),
						message: $('[name="message"]').val(),
						company: $('[name="company_name"]').val()						
					},
					callback: (r) => {
						if(r.message==="okay"){
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
								
							$form.find('.form-control').removeClass('error');

							$submitButton.val( submitButtonText ).attr('disabled', false);
							return;
						} else {
							$errorMessage.html(data.errorMessage).show();
							console.log(r.exc);
						}
						$messageError.removeClass('d-none');
						$messageSuccess.addClass('d-none');

						$form.find('.has-success')
							.removeClass('has-success');
							
						$submitButton.val( submitButtonText ).attr('disabled', false);
					}
				});
				
				return false;
			}
		});
	});
	

});


