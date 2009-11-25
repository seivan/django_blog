$(function() {
    // // Use this example, or...
    // $('a[@rel*=lightbox]').lightBox(); // Select all links that contains lightbox in the attribute rel
    // // This, or...
    // $('#gallery a').lightBox(); // Select all links in object with gallery ID
    // // This, or...
	$('a.lightbox').lightBox({
    imageLoading: '/seivanheidari_media/javascript/lib/css/images/lightbox-ico-loading.gif',
    imageBtnClose: '/seivanheidari_media/javascript/lib/css/images/lightbox-btn-close.gif',
    imageBtnPrev: '/seivanheidari_media/javascript/lib/css/images/lightbox-btn-prev.gif',
    imageBtnNext: '/seivanheidari_media/javascript/lib/css/images/lightbox-btn-next.gif',
	}); // Select all links with lightbox class
    // // This, or...
    // $('a').lightBox(); // Select all links in the page
    // // ... The possibility are many. Use your creative or choose one in the examples above
});