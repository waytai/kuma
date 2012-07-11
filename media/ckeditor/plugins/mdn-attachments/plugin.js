
CKEDITOR.plugins.add('mdn-attachments', {
        init: function(editor) {

        	// Utility method for updating the attachments dropdown
        	// Should be used within the mdn-link and image dialogs
        	CKEDITOR.mdn.updateAttachments = function(select, filter) {
        		if(!select) return;

				var attachmentsArray = [],
					mdnArray = window.MDN_ATTACHMENTS;

				// Clear the select
				select.clear();
				if(mdnArray) {
					jQuery.each(mdnArray, function() {
						if(!filter || filter(this)) {
							select.add(this.title, this.url);
						}
					});
				}

				if(!attachmentsArray.length) {
					select.add(gettext('No attachments available'), '');
				}
			}

        }
});