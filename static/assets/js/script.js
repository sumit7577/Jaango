$(document).ready(function(){

    $("#expand-footer-btn").click(function () {
        $(".footer-wrapper.stick-bottom").toggleClass("expand");
    })

    // Plain JS:
    var el = $('.ul-multiple-checkbox');
    el.scrollTop = 1;
    el.scrollTop = 0;

// jQuery:
    $('.ul-multiple-checkbox').scrollTop(1).scrollTop(0);

    $(document).ajaxStart(function(){
        if($('.loader').length <= 0) {
            $("body").append('<div id="loader-container"  class="loader"><img class="loading-image" src="/static/assets/images/loader.gif" alt="loading.."></div>');
            $('.loader').show();
        }
    });

    $(document).ajaxStop(function(){
        $('.loader').hide();
        $("#loader-container").remove();
    });

    setDefaultCarouselHeight();

    setInnerCarouselHeight();

    //form validator
    $.validate({
        errorMessagePosition : 'inline',
        modules :  'security, logic, file',
        form : '#frm-bi, #form-user-login, #form-user-register, #forgot-password, #contact-property-form, #individualuser-settings-form, #company-settings-form, #property-registration-form, #update-property-registration-form, #service-registration-form, #update-service-registration-form, #material-registration-form, #update-material-registration-form, #add-property-category-form, #add-material-category-form, #add-service-category-form, #structure-registration-form, #structure-update-form, #equipment-registration-form, #equipment-update-form, #form-change-password, #contact-service-form, .form-user-register',
        showErrorDialogs : true
    });
//disabledFormFilter : '#form-user-register, #individualuser-settings-form, #company-settings-form, #property-registration-form, #update-property-registration-form, #service-registration-form, #update-service-registration-form, #material-registration-form, #update-material-registration-form, #add-property-category-form, #add-material-category-form, #add-service-category-form, .inline-label-form, #contact-property-form, #structure-registration-form, #structure-update-form, #equipment-registration-form, #equipment-update-form, #form-change-password, #form-user-password-reset',
    //show footer only after page loads
    $(document).ready(function() {
        $('footer').show();
    });

    //disabling user from dragging elements
    $('*').on('dragstart', function(event) { event.preventDefault(); });



    //image thumbnail file input
    $(function() {
        $(".image-container-bi").on("change", '.uploadFile', function() {
            var objFile =  $(this);
            var files = !!this.files ? this.files : [];
            if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support

            if (/^image/.test( files[0].type)){// only image file
                var reader = new FileReader();// instance of the FileReader
                reader.readAsDataURL(files[0]); // read the local file

                reader.onloadend = function () {   // set image data as background of div
                    var fileSize = files[0].size;
                    objFile.siblings('.error-file-size').hide();
                    if (fileSize / (1024 * 1024) > 3) {
                        resetImage(objFile);
                        objFile.siblings('.error-file-size').text("Banner Image must be under 3MB ").show();
                    }
                    else {
                        objFile.next(".file-input-button").css("background-image", "url(" + this.result + ")");
                        objFile.next(".file-input-button").find(".fa-plus-circle").addClass("fa-times-circle");
                        objFile.next(".file-input-button").find(".fa-plus-circle").removeClass("fa-plus-circle");
                    }
                };

                var img = new Image();
                img.onload = function () {
                    // if ((this.width > 500) || (this.height > 400)) {
                    //     resetImage(objFile);
                    //     objFile.siblings('.error-file-size').text("Image dimension should be under 500px x 400px ").show();
                    // }
                };
                var _URL = window.URL || window.webkitURL;
                img.src = _URL.createObjectURL(files[0]);

            }
        });

        $(".image-container-bi").on("click", '.uploadFile', function(e) {
            var objFile =  $(this);
            var files = !!this.files ? this.files : [];
            if (!files.length || !window.FileReader){
                // do selection
            }else{
                e.preventDefault();
                resetImage(objFile);
            }
        });
    });

    //Solution to modal padding left issue

    $('.modal').on('show.bs.modal', function () {
        if ($(document).height() > $(window).height()) {
            // no-scroll
            $('body').addClass("modal-open-noscroll");
        }
        else {
            $('body').removeClass("modal-open-noscroll");
        }
    });

    $('.modal').on('hide.bs.modal', function () {
        $('body').removeClass("modal-open-noscroll");
    });

    // error msg in forms
    $('.search-filters-submit').click(function () {
        $('.error-msg').addClass('hidden');
    });
    $('.close').click(function () {
        $('.error-msg').addClass('hidden');
    });

    $('#login-button').click(function () {
        reset_values_at_login_button_click();
        $( ".form-error" ).remove();
        $("input").css("border", "1px solid #02acfa");
    });

    userLoginWidget();

    $('.register-modal').bind('hidden.bs.modal', function () {
        $("html").css("margin-right", "0px");
    });
    $('.register-modal').bind('show.bs.modal', function () {
        $("html").css("margin-right", "-15px");
    });

    //scripts for user profile

    $('#cancel-settings-u').click(function() {
        $('.user-settings').addClass('hidden');
        $('.profile-view').removeClass('hidden');
    });

    $('#add-property-button').click(function(){
        $('#property-registration-div').removeClass('hidden');
    });

    $('#add-more-properties-button').click(function () {

        $('#user-property-list').addClass('hidden');
        $('#property-registration-div').removeClass('hidden');
    });

    $('#add-more-services-button').click(function () {
        $('#user-services-list').addClass('hidden');
        $('#service-registration-div').removeClass('hidden');
    });

    $('#add-materials-button').click(function(){
        $('#nil-materials').addClass('hidden');
        $('#materials-registration-div').removeClass('hidden');
    });

    $('#property-reg-form-close-btn').click(function () {
        showPropertiesList();
    });

    // logout
    $('#contact-signin').hover(function () {
        $('#dropdown-header').addClass('open');
    });

    $('#contact-signin').mouseleave(function () {
        $('#dropdown-header').removeClass('open');
    });

    // logout
    $('#construction-menu-dropdown').hover(function () {
        $(this).addClass('open');
    });

    $('#construction-menu-dropdown').mouseleave(function () {
        $(this).removeClass('open');
    });

});

function userLoginWidget() {
    var _this = this;
    _this.userid = $.cookie('userid');
    if (_this.userid == null || _this.userid == undefined) {
        $('#contact-signin').addClass('hidden');
        $('#login-button').removeClass('hidden');
        $('.wrap-dynamic-div').removeClass('hidden');
    }
    else {
        $('#login-button').addClass('hidden');
        $('#contact-signin').removeClass('hidden');
        $('.wrap-dynamic-div').removeClass('hidden');
    }
}

function showPropertiesList(){
    $('#nil-properties').addClass('hidden');
    $('#property-registration-div').addClass('hidden');
    $('#update-property-registration-div').addClass('hidden');
    $('#user-property-view').addClass('hidden');
    $('#user-property-list').removeClass('hidden');
}


function showPropertiesListAdmin(){
    $('#nil-properties').addClass('hidden');
    $('#property-registration-div').addClass('hidden');
    $('#property-registration-div-admin').addClass('hidden');
    $('#update-property-registration-div').addClass('hidden');
    $('#update-property-registration-div-admin').addClass('hidden');
    $('#user-property-view').addClass('hidden');
    $('#user-property-list').addClass('hidden');
    $('#property-management').removeClass('hidden');
}

function reset_values_at_login_button_click() {
    $(".twitter-modal-general-internal").addClass("hidden");
    $(".twitter-signup-modal-general-internal").addClass("hidden");
    $(".modal-general-internal").removeClass("hidden");
    $('#login-error').addClass('hidden');
    $('#register-messages').addClass('hidden');
    $('#form-user-register').find('input:text').val('');
    document.getElementById('email-register').value='';
    document.getElementById('email-login').value='';
    document.getElementById('password-register').value='';
    document.getElementById('password-login').value='';
    $('#user-individual').prop("checked", true);
}

function showEmptyPropertyMessage(){
    $('#nil-properties').removeClass('hidden');
    $('#user-property-list').addClass('hidden');
    $('#property-registration-div').addClass('hidden');
    $('#user-property-view').addClass('hidden');
}


function showPropertyEdit(){
    $('#user-property-view').removeClass('hidden');
    $('#property-info').removeClass('hidden');
    $('#view-property-details').removeClass('hidden');
    $('#update-property-registration-div').addClass('hidden');
}

function showPropertyInfoAdmin(){
    $('#update-property-registration-div-admin').addClass('hidden');
    $('#property-info').removeClass('hidden');
}

function showMaterialView() {
    $('#material-details').removeClass('hidden');
    $('#user-materials-list').addClass('hidden');
    $('#user-materials').addClass('hidden');
}

function propertyEdit(){
    //$('#user-property-view').removeClass('hidden');
    $('#view-property-details').addClass('hidden');
    $('#update-property-registration-div').removeClass('hidden');
}

function showServiceInfo(){
    $('#user-service-view').removeClass('hidden');
    $('#view-service-details').removeClass('hidden');
    $('#service-details-update-div-admin').addClass('hidden');
    $('#service-info').removeClass('hidden');
    $('#nil-services').addClass('hidden');
    $('#user-services-list').addClass('hidden');
    // $('#user-services-list').removeClass('hidden');
    $('#service-details-update-div').addClass('hidden');
    $('#update-service-registration-form').addClass('hidden');
}

function showMaterialEdit(){
    $('#user-material-view').removeClass('hidden');
    $('#view-material-details').removeClass('hidden');
    $('#material-details-update-div').addClass('hidden');
    $('#update-material-registration-form').addClass('hidden');
}

function showServiceList(){

    $('#nil-services').addClass('hidden');
    $('#service-registration-div').addClass('hidden');
    $('#user-service-view').addClass('hidden');
    $('#user-services-list').removeClass('hidden');
    $('#service-details-update-div').addClass('hidden');
    $('#update-service-registration-form').addClass('hidden');
    // $('#service-info').addClass('hidden');
}

function showEmptyService() {
    $('#nil-services').removeClass('hidden');
    $('#service-registration-div').addClass('hidden');
    $('#user-service-view').addClass('hidden');
    $('#user-services-list').addClass('hidden');
    $('#service-details-update-div').addClass('hidden');
    $('#update-service-registration-form').addClass('hidden');
    // $('#service-info').addClass('hidden');
}

function showMaterialList() {
    $('#nil-materials').addClass('hidden');
    $('#user-material-view').addClass('hidden');
    $('#material-details-update-div').addClass('hidden');
    $('#user-materials-list').removeClass('hidden');
    $('#materials-registration-div').addClass('hidden');
}

function showEmptyMaterialList() {
    $('#nil-materials').removeClass('hidden');
    $('#user-material-view').addClass('hidden');
    $('#material-details-update-div').addClass('hidden');
    $('#user-materials-list').addClass('hidden');
    $('#materials-registration-div').addClass('hidden');
}

//Admin ops

function adminViewPropertyInfo() {
    $('#property-management').addClass('hidden');
    $('#property-info').removeClass('hidden');
}

function showAdminPropertyTable() {
    $('#property-management').removeClass('hidden');
    $('#property-info').addClass('hidden');
    $('#property-category-management').addClass('hidden');
    $('#update-property-registration-div-admin').addClass('hidden');
}

function showPropertyTypesManagement() {
    $('#property-management').addClass('hidden');
    $('#add-property-category-form').addClass('hidden');
    $('#property-category-management').removeClass('hidden');
    $('#add-new-property-category').removeClass('hidden');

}

function adminViewServiceInfo() {
    $('#services-management').addClass('hidden');
    $('#service-info').removeClass('hidden');
}



function showAdminServiceTable() {
    $('#services-management').removeClass('hidden');
    $('#service-registration-div-admin').addClass('hidden');
    $('#service-details-update-div-admin').addClass('hidden');
    $('#service-info').addClass('hidden');
    $('#service-category-management').addClass('hidden');
    $('#service_cat_back_btn').addClass('hidden');
}

function showServiceCategoryManagement() {
    $('#services-management').addClass('hidden');
    $('#service-category-management').removeClass('hidden');
    $('#service_cat_back_btn').removeClass('hidden');
    $('#add-new-service-category').removeClass('hidden');
    $("#add-service-category-form").addClass('hidden');
}

function adminViewMaterialInfo() {
    $('#materials-management').addClass('hidden');
    $('#material-info').removeClass('hidden');
    $('#update-material-registration-form-admin').addClass('hidden');
}

//admin materials
function showAdminMaterialsTable() {
    $('#materials-management').removeClass('hidden');
    $('#material-info').addClass('hidden');
    $('#material-category-management').addClass('hidden');
    $('#materials-registration-div-admin').addClass('hidden');
    $('#material-details-update-div-admin').addClass('hidden');
}

function showAdminShareRentFlatTable() {
    $('#admin-flat-table').removeClass('hidden');
    // $('#material-info').addClass('hidden');
    // $('#material-category-management').addClass('hidden');
}

function showCategoryManagement() {
    $('#material-category-management').removeClass('hidden');
    $("#add-new-material-category").removeClass('hidden');
    $("#add-material-category-form").addClass('hidden');
    $('#materials-management').addClass('hidden');
}
function afterCancelAddCategoryButton() {
    $("#add-material-category-form").addClass('hidden');
    $("#add-new-material-category").removeClass('hidden');
    $("#materials-category-list-table").removeClass('hidden');
}

function showNewCategoryForm() {
    $("#materials-category-list-table").addClass('hidden');
    $("#add-new-material-category").addClass('hidden');
    $("#add-material-category-form").removeClass('hidden');

}

function showNewServiceForm() {
    $("#service-category-list-table").addClass('hidden');
    $("#add-service-category-form").removeClass('hidden');
}

function adminViewUserInfo(usertype) {
    $('#user-management').addClass('hidden');
    $('#user-info').css('display','block');
    $('#material-category-management').removeClass('hidden');

    if (usertype == 'individual') {
        $('#individual-info-tbl').removeClass('hidden');
        $('#company-info-tbl').addClass('hidden');
    }else {
        $('#company-info-tbl').removeClass('hidden');
        $('#individual-info-tbl').addClass('hidden');
    }
}

function showAdminUsersTable() {
    $('#user-management').removeClass('hidden');
    $('#user-info').css('display','none');
    $('#material-category-management').removeClass('hidden');
}

function initMap() {
    var mapDiv = document.getElementById('map');
    var map = new google.maps.Map(mapDiv, {
        center: {lat: 44.540, lng: -78.546},
        zoom: 5
    });
}

function setDefaultCarouselHeight() {
    var divWidth = $('.default-carousel').width();
    var carouselInner = divWidth/2.90909090909;
    $('.default-carousel').height(carouselInner);
}

function setInnerCarouselHeight() {
    var divWidth = $('.inner-page-carousel').width();
    var carouselInner = divWidth/5;
    $('.inner-page-carousel').height(carouselInner);
}

$(window).resize(function(){
    setDefaultCarouselHeight();
    setInnerCarouselHeight();
});

$( window ).load(function() {

    // window.setTimeout( materialFooter, 5000 ); // 5 seconds

    $('#loading-indicator').addClass('hidden');
    $('#myCarousel').carousel({
        interval: 6000,
        cycle: true
    });
});

function resetImage(objFile){
    objFile.val('');
    objFile.next(".file-input-button").css("background-image", "url('')");
    objFile.next(".file-input-button").find(".fa-times-circle").addClass("fa-plus-circle");
    objFile.next(".file-input-button").find(".fa-plus-circle").removeClass("fa-times-circle");
}

function materialFooter() {
    var speed = 5;
    var items, scroller = $('#scroller');
    var width = 0;
    scroller.children().each(function(){
        width += $(this).outerWidth(true);
    });

    var widthScrollerWrapper = $('#scrollerWrapper').width();
    if (widthScrollerWrapper < width) {
        scroller.css('width', width);
        scroll();
    }
    else {
        scrollElse();
    }

    function scroll(){
        items = scroller.children();
        var scrollWidth = items.eq(0).outerWidth();
        scroller.animate({'left' : 0 - scrollWidth}, scrollWidth * 100 / speed, 'linear', changeFirst);
    }

    function changeFirst(){
        scroller.append(items.eq(0).remove()).css('left', 0);
        scroll();
    }

    function scrollElse() {
        // console.log('width=' + width);
        items = scroller.children();
        scroller.animate({'left' : 0 - width}, width * 100 / speed, 'linear', changeFirstElse);
    }

    function changeFirstElse(){
        scroller.append(items.eq(0).remove()).css('left', width);
        scrollElse();
    }
}

$(window).scroll(function() {
    if ($(this).scrollTop() >= 100) {        // If page is scrolled more than 50px
        $('#return-to-top').fadeIn(200);    // Fade in the arrow
    } else {
        $('#return-to-top').fadeOut(200);   // Else fade out the arrow
    }
});

$('#return-to-top').click(function() {      // When arrow is clicked
    $('html, body').animate({'scrollTop': 0}, 500);
    return false;
});
