/**
 *Flats page related operations
 */
 "use strict";
 _.templateSettings = {
     interpolate: /\[\[\=(.+?)\]\]/gim,
     evaluate: /\[\[(.+?)\]\]/gim,
     escape: /\[\[\-(.+?)\]\]/gim
 };
 _.templateSettings.variable = 'rc';
 
 (function(){
     var FlatsShareUserOperations;
     $("#deposit-error").hide();
     $("#rent-error").hide();
     $("#min-max-error").hide();
     FlatsShareUserOperations = (function(){
         FlatsShareUserOperations.prototype = Object.create(Main.prototype);
 
         function FlatsShareUserOperations(){
             var _this = this;
             this.events = [];
             this.init();
         }
 
         FlatsShareUserOperations.prototype.init = function () {
             var _this = this;
             _this.loadDefaultData();
             _this.setDefaultContactInfo();
             var csrftoken = $.cookie('csrftoken');
             _this.userid = $.cookie('userid');
             _this.usertype = $.cookie('usertype');
             _this.limit = 4;
             _this.page = 1;
             _this.apiUrl = "/flat/registration/";
             _this.jsonData = {};
 
             _this.available = "";
             _this.minimum_term = "";
             _this.maximum_term = "";
             _this.short_lets_considered = "";
             _this.bills_included = "";
             _this.ensuite_toilet = "";
             _this.furnishings = "";
             _this.parking = "";
             _this.garage = "";
             _this.garden_or_terrace = "";
             _this.balcony_or_patio = "";
             _this.living_room = "";
             _this.broadband_included = "";
             _this.housemates = "";
             _this.total_rooms = "";
             _this.ages = "";
             _this.smoker = "";
             _this.any_pets = "";
             _this.language = "";
             _this.occupation = "";
             _this.gender = "";
             _this.couples_ok = "";
             _this.pets_ok = "";
             _this.smoking_ok = "";
             _this.new_housemate_occupation = "";
             _this.references = "";
             _this.min_age = "";
             _this.new_housemate_gender = "";
             _this.share_or_rent = "";
             _this.flat_image = "";
             _this.city = "";
             _this.description = "";
             _this.address = "";
             _this.rent_expected = "";
             _this.currency_type = "";
             _this.room_deposit_index = 1;
             _this.room_rent_index = 1;
 
 
             $.ajaxSetup({
                 beforeSend: function(xhr, settings) {
                     if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                         xhr.setRequestHeader("X-CSRFToken", csrftoken);
                     }
                 }
             });
 
             function csrfSafeMethod(method) {
                 // these HTTP methods do not require CSRF protection
                 return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
             }
 
             _this.userCategory = $.cookie('userCategory');
             if (typeof _this.userCategory == 'undefined'){
                 $('.login-modal').modal('show');
 
                 // On Register/Forgot Password redirect to home
                 $("#login-form-signup-link").attr("href","/?action=register");
                 $("#login-form-signup-link").removeAttr("data-toggle");
                 $("#login-form-signup-link").removeAttr("data-target");
                 $("#login-form-signup-link").removeAttr("data-dismiss");
 
                 $("#login-form-forgot-password-link").attr("href","/?action=forgot-password");
                 $("#login-form-forgot-password-link").removeAttr("data-toggle");
                 $("#login-form-forgot-password-link").removeAttr("data-target");
                 $("#login-form-forgot-password-link").removeAttr("data-dismiss");
             }
 
             // load lists
             _this.loadList("/api/admin/location/","#lst-location-bi","city","city",_this.location);
             //_this.renderList(_this.dataListRooms,"#lst-rooms-bi","Id","Name",_this.rooms);
 
             _this.renderList(_this.dataListTerm,"#lst-minimum-term-av","Id","Name",_this.term);
             _this.renderList(_this.dataListTerm,"#lst-maximum-term-av","Id","Name",_this.term);
             _this.renderList(_this.dataListCurrency,"#lst-currency-share","Id","Name","NGN");
 
             //_this.renderList(_this.dataListHouseMates,"#lst-housemates-h","Id","Name",_this.term);
             _this.renderList(_this.dataListOccupation,"#lst-occupation-h","Id","Name",_this.occupation);
             _this.renderList(_this.dataListGender,"#lst-gender-h","Id","Name",_this.gender);
 
             _this.renderList(_this.dataListOccupation,"#lst-occupation-p","Id","Name",_this.occupation);
             _this.renderList(_this.dataListGender,"#lst-gender-p","Id","Name",_this.gender);
 
 
 
             // fill page with dynamic values
             _this.displayBanner();
             _this.displayFooter();
 
 
 
             $("#frm-bi").submit(function(e){
                 e.preventDefault();
                 if( $(this).isValid() ) {
                     // Make sure Area and City Captured from Location Autocomplete
                     if(_this.city) {
                         $('#step2').tab('show');
                     }
                     else {
                         alert("We could'nt fetch City from location. Try searching your area/city")
                     }
                 }
             });
 
 
             $("#frm-av").submit(function(e){
                 e.preventDefault();
                 _this.minimum_term =  $('#lst-minimum-term-av').val();
                 _this.maximum_term =  $('#lst-maximum-term-av').val();
                 if(parseInt(_this.minimum_term) > parseInt(_this.maximum_term)) {
                     // $("#lst-maximum-term-av").val("");
                     $("#min-max-error").show();
                     $('#lst-maximum-term-av').selectpicker('refresh');
                     $(this).isValid();
                 }else{
                     if( $(this).isValid() ) {
                         if( $(this).isValid() ) {
                             var roomsForShare =  $("#txt-rooms-bi").val();
                             if( ($("h5[name='room-index[]'").length) == roomsForShare ){
                                 $("#deposit-error").hide();
                                 $("#min-max-error").hide();
                             }
                             else{
                                 $("#deposit-error").show();
                                 $("#min-max-error").hide();
                             }
                             if( ($("h5[name='rent-index[]'").length) == roomsForShare ){
                                 $("#rent-error").hide();
                                 $("#min-max-error").hide();
                             }
                             else{
                                 $("#rent-error").show();
                                 $("#min-max-error").hide();
                             }
                             if(($("h5[name='room-index[]'").length) == roomsForShare && ($("h5[name='rent-index[]'").length) == roomsForShare){
                                 $('#step3').tab('show');
                             }
                         }
                     }
                 }
             });
 
 
 
 
             $("#frm-am").submit(function(e){
                 e.preventDefault();
                 if( $(this).isValid() ) {
                     $('#step4').tab('show');
                 }
             });
 
             $("#frm-h").submit(function(e){
                 e.preventDefault();
                 if( $(this).isValid() ) {
                     $('#step5').tab('show');
                 }
             });
 
 
             $("#frm-p").submit(function(e){
                 e.preventDefault();
                 if( $(this).isValid()) {
                     _this.registerShareFlat();
                 }
             });
 
 
 
             $('.login-modal').on('hidden.bs.modal', function () {
                 _this.userCategory = $.cookie('userCategory');
                 if (typeof _this.userCategory == 'undefined'){
                     $('.login-modal').modal('hide');
                     window.location.href = '/';
                 }
             });
 
 
             $('#btn-show-basic-info-previous').click(function (e) {
                 e.preventDefault();
                 $("#deposit-error").hide();
                 $("#rent-error").hide();
                 $("#min-max-error").hide();
                 $('#step1').tab('show');
             });
 
             $('#btn-show-availability-previous').click(function (e) {
                 e.preventDefault();
                 $('#step2').tab('show');
             });
 
             $('#btn-show-amenities-previous').click(function (e) {
                 e.preventDefault();
                 $('#step3').tab('show');
             });
 
             $('#btn-show-household-previous').click(function (e) {
                 e.preventDefault();
                 $('#step4').tab('show');
             });
 
 
             $('#txt-rooms-bi').on( "change",  function(e)  {
                 e.preventDefault();
                 // $('#room-deposit-container').html("");
                 // $('#room-deposit-container').empty();
                 // _this.room_deposit_index = 1;
             });
 
 
 
             $('#btn-add-room-deposit').click(function (e) {
                 var intRooms = $("#txt-rooms-bi").val();
                 if(intRooms < 1){
                     intRooms = 0;
                 }else{
                     intRooms = intRooms - 1;
                 }
 
                 if(($("h5[name='room-index[]'").length + 1) == $("#txt-rooms-bi").val() ){
                     $("#deposit-error").hide();
                 }
 
                 if($("h5[name='room-index[]'").length <= intRooms){
                     var templateDatacontent = {
                         room_index: (_this.room_deposit_index + 1)
                     };
 
                     var flatRoomDepositContainer = $('#room-deposit-container');
                     var flatRoomDepositTemplate = _.template(
                         $('script#room-deposit-template').html()
                     );
                     flatRoomDepositContainer.append(
                         flatRoomDepositTemplate(templateDatacontent)
                     );
                     _this.room_deposit_index++;
                 }
 
             });
 
             $('#btn-add-room-rent').click(function (e) {
                 var intRooms = $("#txt-rooms-bi").val();
                 if(intRooms < 1){
                     intRooms = 0;
                 }else{
                     intRooms = intRooms - 1;
                 }
 
                 if(($("h5[name='rent-index[]'").length + 1) == $("#txt-rooms-bi").val() ){
                     //console.log("rents === rooms")
                     $("#rent-error").hide();
                 }
                 //console.log("h5 < intRooms", $("h5[name='rent-index[]'").length, intRooms)
                 if($("h5[name='rent-index[]'").length <= intRooms){
                     var templateDatacontent = {
                         rent_index: (_this.room_rent_index + 1)
                     };
 
                     var flatRoomRentContainer = $('#room-rent-container');
                     var flatRoomRentTemplate = _.template(
                         $('script#room-rent-template').html()
                     );
                     flatRoomRentContainer.append(
                         flatRoomRentTemplate(templateDatacontent)
                     );
                     _this.room_rent_index++;
                 }
 
              });
 
 
 
 
             $('#room-deposit-container').on( "click", ".delete_room_deposit", function(e)  {
                 e.preventDefault();
                 if(($("h5[name='room-index[]'").length -1) == $("#txt-rooms-bi").val() ){
                     $("#deposit-error").hide();
                 }
 
                  _this.deleteElement = $(this).parent().parent();
                 $("#flat-deposit-delete-modal-u").modal("show");
 
 
                 $('#delete-flat-deposit-y-u').click(function () {
                     $("#flat-deposit-delete-modal-u").modal("hide");
                     _this.deleteElement.remove();
                     _this.reIndexRoom();
 
                 });
 
                 $('delete-flat-deposit-n').click(function () {
                     $("#flat-deposit-delete-modal-u").modal("hide");
                     _this.deleteId = "";
                     _this.deleteElement = "";
                     _this.share_or_rent = "";
                 });
             });
 
             $('#room-rent-container').on( "click", ".delete_room_rent", function(e)  {
                 e.preventDefault();
                 if(($("h5[name='rent-index[]'").length -1) == $("#txt-rooms-bi").val() ){
                     $("#rent-error").hide();
                 }
 
                  _this.deleteElement = $(this).parent().parent();
                 $("#flat-rent-delete-modal-u").modal("show");
 
 
                 $('#delete-flat-rent-y-u').click(function () {
                     $("#flat-rent-delete-modal-u").modal("hide");
                     _this.deleteElement.remove();
                     _this.reIndexRent();
 
                 });
 
                 $('delete-flat-rent-n').click(function () {
                     $("#flat-rent-delete-modal-u").modal("hide");
                     _this.deleteId = "";
                     _this.deleteElement = "";
                     _this.share_or_rent = "";
                 });
             });
 
 
             //Location Search Autocomplete with Google Places API
 
 
             var locationInput = document.getElementById('location-autocomplete-share');
             var area= "", city= "", state = "";
             var options = {
               // types: ['(cities)'],
               componentRestrictions: {country: 'ng'},
             };
 
             var autocomplete = new google.maps.places.Autocomplete(locationInput, options);
             google.maps.event.addListener(autocomplete, 'place_changed', function() {
                 area= "", city= "", state = "";
                 var place = autocomplete.getPlace();
                 place.address_components.forEach((component) => {
                     if (component.types.includes("sublocality")) {
                         area = component.long_name;
                     } else if (component.types.includes("locality")) {
                             city = component.long_name;
                     } else if (component.types.includes("administrative_area_level_3")) {
                         if (!city) {
                             city = component.long_name;
                         }
                     } else if (component.types.includes("administrative_area_level_1")) {
                         state = component.long_name;
                     }
                 });
                 //console.log("area:", area, "\ncity:", city, "\nstate:", state);
                 _this.city = city;
                 _this.area = area;
                 _this.state = state;
                 if(!city){
                     alert("We could'nt fetch City from location. Try searching area/city");
                 }
             })
 
 
         };
 
 
         FlatsShareUserOperations.prototype.reIndexRoom = function() {
             var _this = this;
             _this.room_deposit_index = 0;
             $.each($("h5[name='room-index[]'"), function(i, obj) {
                 $(this).html("Room " + (_this.room_deposit_index+1));
                 _this.room_deposit_index++;
             });
 
         };
 
         FlatsShareUserOperations.prototype.reIndexRent = function() {
             var _this = this;
             _this.room_rent_index = 0;
             $.each($("h5[name='rent-index[]'"), function(i, obj) {
                 $(this).html("Room " + (_this.room_rent_index+1));
                 _this.room_rent_index++;
             });
 
         };
 
 
         // display  banner
         FlatsShareUserOperations.prototype.displayBanner = function() {
             var _this = this;
             var url ="/banner/fetch-banners/";
             $.ajax({
                 url: url,
                 method: 'GET',
                 header: {}, contentType: 'application/json',
                 dataType: "json"
             }).done(function(response){
                 if(response.flat_banners.length > 0){
                     var bannerImageUrl = "/static/assets/images/"+response.flat_banners[0].banner_value ;
                     $("#banner-image").attr("src",bannerImageUrl);
                 }
 
             });
 
         };
 
         // load list
         FlatsShareUserOperations.prototype.loadList = function(url,elem,idName,valueName,selectedValue) {
             var _this = this;
             var url =url;
             $.ajax({
                 url: url,
                 method: 'GET',
                 header: {}, contentType: 'application/json',
                 dataType: "json"
             }).done(function(response){
                 _this.renderList(response,elem,idName,valueName, selectedValue);
             });
 
         };
 
 
         FlatsShareUserOperations.prototype.renderList = function(response,elem,idName,valueName,selectedValue) {
 
             var listElement = $(elem);
             var listSelected = "";
             listElement.html("");
             for(var i = 0;i< response.length;i++){
                 if(selectedValue == response[i][idName] ){
                     listSelected = "selected";
                 }else{
                     listSelected = "";
                 }
                 listElement.append('<option value="'+response[i][idName]+'" '+listSelected+' >'+response[i][valueName]+'</option>');
             }
             listElement.selectpicker('refresh');
         };
 
         FlatsShareUserOperations.prototype.getUrlParameter = function(sParam) {
             var sPageURL = decodeURIComponent(window.location.search.substring(1)),
                 sURLVariables = sPageURL.split('&'),
                 sParameterName,
                 i;
 
             for (i = 0; i < sURLVariables.length; i++) {
                 sParameterName = sURLVariables[i].split('=');
 
                 if (sParameterName[0] === sParam) {
                     return sParameterName[1] === undefined ? true : sParameterName[1];
                 }
             }
         };
 
         FlatsShareUserOperations.prototype.loadDefaultData = function() {
             var _this = this;
             _this.dataListPrice = [
                 { Id: "0,1000", Name: " < 1000 " },
                 { Id: "1000,10000", Name: "1000 - 10000" },
                 { Id: "10000,20000", Name: "10000 - 20000" },
                 { Id: "20000,", Name: " > 20000 " }
             ];
 
             _this.dataListSize = [
                 { Id: "0,500", Name: " < 500" },
                 { Id: "500,1000", Name: "500 - 1000" },
                 { Id: "1000,2000", Name: "1000 - 2000 " },
                 { Id: "2000,", Name: " > 2000 " }
             ];
 
             _this.dataListRooms = [
                 { Id: "1", Name: "1" },
                 { Id: "2", Name: "2" },
                 { Id: "3", Name: "3" },
                 { Id: "4", Name: "4" },
                 { Id: "5", Name: "5" },
                 { Id: "6", Name: "5+" }
 
             ];
 
             _this.dataListShareOrRent = [
                 { Id: "share", Name: "Share" },
                 { Id: "rent", Name: "Rent" }
             ];
 
             _this.dataListGender = [
                 { Id: "couple", Name: "Couple" },
                 { Id: "male", Name: "Male" },
                 { Id: "male/female", Name: "Either Male or Female" },
                 { Id: "female", Name: "Female" },
                 { Id: "na", Name: "Any" }
             ];
 
             _this.dataListCurrency = [
                 { Id: "NGN", Name: "â‚¦ NGN" },
                 { Id: "USD", Name: "$ USD" },
                 { Id: "GBP", Name: "Â£ GBP" },
                 { Id: "EUR", Name: "â‚¬ EUR" }
             ];
 
             _this.dataListTerm = [
                 { Id: "1", Name: "1 Month" },
                 { Id: "2", Name: "2 Months" },
                 { Id: "3", Name: "3 Months" },
                 { Id: "4", Name: "4 Months" },
                 { Id: "5", Name: "5 Months" },
                 { Id: "5", Name: "6 Months" },
                 { Id: "7", Name: "7 Months" },
                 { Id: "8", Name: "8 Months" },
                 { Id: "9", Name: "9 Months" },
                 { Id: "10", Name: "10 Months" },
                 { Id: "11", Name: "11 Months" },
                 { Id: "12", Name: "1 Year" },
                 { Id: "18", Name: "1.5 Years" },
                 { Id: "24", Name: "2 Years" },
                 { Id: "25", Name: "2+ Years" }
             ];
 
             _this.dataListBillsIncluded = [
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
 
             _this.dataListShortLetsConsidered = [
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
             _this.dataListEnsuiteToilets = [
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
 
             _this.dataListFurnishings = [
                 { Id: "fully furnished", Name: "Fully Furnished" },
                 { Id: "partially furnished", Name: "Partially Furnished" },
                 { Id: "not furnished", Name: "Not Furnished" }
             ];
 
             _this.dataListParking = [
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
 
             _this.dataListGarage = [
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
 
             _this.dataListGardenTerrace = [
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
 
             _this.dataListGarage = [
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
 
             _this.dataListBalconyPatio = [
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
 
             _this.dataListLivingRoom = [
                 { Id: "shared", Name: "Shared" },
                 { Id: "not shared", Name: "Not Shared" }
             ];
 
             _this.dataListBroadband = [
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
 
             _this.dataListSmokers = [
                 { Id: "don't mind", Name: "Don't Mind" },
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
 
             _this.dataListPets = [
                 { Id: "don't mind", Name: "Don't Mind" },
                 { Id: "True", Name: "Yes" },
                 { Id: "False", Name: "No" }
             ];
 
             _this.dataListOccupation = [
                 { Id: "don't mind", Name: "Don't Mind" },
                 { Id: "students", Name: "Students" },
                 { Id: "professionals", Name: "Professionals" }
             ];
 
             _this.dataListHouseMates = [
                 { Id: "1", Name: "1" },
                 { Id: "2", Name: "2" },
                 { Id: "3", Name: "3" },
                 { Id: "4", Name: "4" },
                 { Id: "5", Name: "5" },
                 { Id: "6", Name: "6" },
                 { Id: "7", Name: "7" },
                 { Id: "8", Name: "8" },
                 { Id: "9", Name: "8+" }
 
             ];
 
         };
 
         FlatsShareUserOperations.prototype.setDefaultContactInfo = function () {
             var _this = this;
             var userId = $.cookie('userid');
             var userType = $.cookie('usertype');
 
             if(typeof userId !== "undefined"){
                 _this.getUserInfo(userId);
             }
         };
 
         FlatsShareUserOperations.prototype.getUserInfo = function (userId) {
             var _this = this;
             var url ="/user/profile/"+userId+"/";
             $.ajax({
                 url: url,
                 method: 'GET',
                 header: {}, contentType: 'application/json',
                 dataType: "json"
             }).done(function(response){
                 if (response.status == "success"){
                     // User exists
                     _this.setAgentContactInfo(response.profile_info);
                 }else{
                     // User doesn't exist
                 }
             });
         };
         //    Set Agent Contact Info to the address in profile info
         FlatsShareUserOperations.prototype.setAgentContactInfo = function (profile_info) {
             $("#txt-agent-contact-info-sh").val(profile_info.user.email + "\n" + profile_info.contact_no);
         };
 
 
 
 
         // display  Footer
         FlatsShareUserOperations.prototype.displayFooter = function() {
             var _this = this;
             var url ="/jaango/admin/material/footer/";
             $.ajax({
                 url: url,
                 method: 'GET',
                 header: {}, contentType: 'application/json',
                 dataType: "json"
             }).done(function(response){
                 _this.renderFooter(response);
             });
 
         };
 
         FlatsShareUserOperations.prototype.renderFooter = function(Footers) {
             var footerCaptionContainer = $('.category-name');
             var footerContentContainer = $('.ul-featured-materials');
 
 
             footerCaptionContainer.html("");
             footerContentContainer.html("");
 
 
             var FootersCount = 0;
             var row =0;
             var newDiv= document.createElement('div');
             newDiv.setAttribute('id','scrollerWrapper');
             var cardTitle = newDiv.appendChild(document.createElement('ul'));
             cardTitle.setAttribute('id','scroller');
             for (var key in Footers){
                 if (Footers.hasOwnProperty(key)) {
                     // check materials category with items
                     if( Object.prototype.toString.call( Footers[key] ) === '[object Array]' && Footers[key].length > 0) {
                         // create template data
                         var liheaderList = cardTitle.appendChild(document.createElement('li'));
                         liheaderList.setAttribute('class','li-featured-material');
                         var h5materialTitle = liheaderList.appendChild(document.createElement('h5'));
                         h5materialTitle.setAttribute('class','category-name');
                         h5materialTitle.innerHTML = key.toUpperCase();
                         var ulmaterialList = liheaderList.appendChild(document.createElement("ul"));
                         ulmaterialList.setAttribute('class','ul-featured-materials');
                         var FootersContent = Footers[key];
                         for(row in FootersContent) {
                             var lilistContents = ulmaterialList.appendChild(document.createElement('li'));
                             var alinkAttribute = lilistContents.appendChild(document.createElement('a'));
                             alinkAttribute.setAttribute('href', '/material/material-details/' + FootersContent[row].id + '/');
                             alinkAttribute.append(FootersContent[row].item + (FootersContent[row].quantity + FootersContent[row].weight_or_size) + "- â‚¦" + FootersContent[row].unit_price);
                             lilistContents.appendChild(alinkAttribute);
                         }
                         if (FootersCount == 4 ) {
                             break;
                         }else{
                             FootersCount++;
                         }
 
                     }
                 }
 
             }
             $('.footer-wrapper').append(newDiv);
             window.setTimeout( materialFooter, 4000 );
 
         };
 
         FlatsShareUserOperations.prototype.getRoomCosts = function() {
             var roomData = [];
             var roomDeposit = 0;
             var roomRent = 0;
             var rentInputEls = $("input[name='txt-room-rent[]']");
 
             $.each($("input[name='txt-room-deposit[]']"), function(i, obj) {
                 roomRent = rentInputEls[i].value;
                 //console.log(rentInputEls[i].value);
                 if (obj.value) {
                     roomDeposit = obj.value;
                 } else {
                     roomDeposit = 0;
                 }
                 if (roomDeposit > 0){
                     roomData.push({room: i + 1, deposit: roomDeposit, rent: roomRent});
                 }
             });
             return roomData;
         };
 
 
 
         FlatsShareUserOperations.prototype.prepareShareFlatData = function() {
             var _this = this;
 
             // _this.city = $("#txt-city-bi").val();
             // _this.state = $("#txt-state-bi").val();
             // _this.area = $("#txt-area-bi").val();
             _this.address = $("#txt-address-bi").val();
             _this.total_rooms = $("#txt-rooms-bi").val();
             _this.description = $("#txt-description-bi").val();
             _this.rent_expected = $("#txt-rent-bi").val();
             _this.room_costs = _this.getRoomCosts();
             //console.log("calling getRoomCosts",JSON.stringify(_this.getRoomCosts()))
 
             _this.currency_type = $("#lst-currency-share").val();
             _this.available = $("#txt-available-from-av").val();
             _this.minimum_term = $("#lst-minimum-term-av").val();
             _this.maximum_term = $("#lst-maximum-term-av").val();
             _this.short_lets_considered = $("input:radio[name='radio-short-lets-av']:checked").val();
             _this.extra_cost = $("#txt-extra-costs-av").val();
             _this.bills_included = $("input:radio[name='radio-bills-included-av']:checked").val();
             _this.agentContact = $("#txt-agent-contact-info-sh").val();
 
             _this.ensuite_toilet = $("input:radio[name='radio-ensuite-toilet-am']:checked").val();
             _this.furnishings = $("input:radio[name='radio-furnishings-am']:checked").val();
             _this.parking = $("input:radio[name='radio-parking-am']:checked").val();
             _this.garage = $("input:radio[name='radio-garage-am']:checked").val();
             _this.garden_or_terrace = $("input:radio[name='radio-garden-terrace-am']:checked").val();
             _this.balcony_or_patio = $("input:radio[name='radio-balcony-patio-am']:checked").val();
             _this.living_room = $("input:radio[name='radio-living-room-am']:checked").val();
             _this.broadband_included = $("input:radio[name='radio-broadband-am']:checked").val();
 
             _this.housemates = $("#txt-housemates-h").val();
             _this.ages = $("#txt-age-h").val();
             _this.smoker = $("input:radio[name='radio-smoker-h']:checked").val();
             _this.any_pets = $("input:radio[name='radio-pets-h']:checked").val();
             _this.language = $("#txt-language-h").val();
             _this.occupation = $("#lst-occupation-h").val();
             _this.gender = $("#lst-gender-h").val();
 
             _this.couples_ok = 'True';
             // $("input:radio[name='radio-couples-ok-p']:checked").val();
             _this.smoking_ok = $("input:radio[name='radio-smoking-ok-p']:checked").val();
             _this.pets_ok = $("input:radio[name='radio-pets-ok-p']:checked").val();
             _this.new_housemate_occupation = $("#lst-occupation-p").val();
             _this.references = $("input:radio[name='radio-references-p']:checked").val();
             if ($("#txt-min-age-p").val()) {
                 _this.min_age = $("#txt-min-age-p").val();
             }else{
                 _this.min_age = "0";
             }
 
             _this.new_housemate_gender = $("#lst-gender-p").val();
             _this.share_or_rent = "share";
 
             return {
                 "city" : _this.city,
                 "state" : _this.state,
                 "area" : _this.area,
                 "address" : _this.address,
                 "total_rooms": _this.total_rooms,
                 "description" : _this.description,
                 "rent_expected" : _this.rent_expected,
                 "available" : _this.available,
                 "minimum_term": _this.minimum_term,
                 "maximum_term": _this.maximum_term,
                 "agentContactInfo":_this.agentContact,
                 "short_lets_considered": _this.short_lets_considered,
                 "bills_included": _this.bills_included,
                 "ensuite_toilet": _this.ensuite_toilet,
                 "furnishings": _this.furnishings,
                 "parking": _this.parking,
                 "garage": _this.garage,
                 "garden_or_terrace": _this.garden_or_terrace,
                 "balcony_or_patio": _this.balcony_or_patio,
                 "living_room": _this.living_room,
                 "broadband_included": _this.broadband_included,
                 "housemates": _this.housemates,
                 "ages": _this.ages,
                 "smoker": _this.smoker,
                 "any_pets": _this.any_pets,
                 "language": _this.language,
                 "occupation": _this.occupation,
                 "gender": _this.gender,
                 "couples_ok": _this.couples_ok,
                 "smoking_ok": _this.smoking_ok,
                 "pets_ok": _this.pets_ok,
                 "new_housemate_occupation": _this.new_housemate_occupation,
                 "references": _this.references,
                 "min_age": _this.min_age,
                 "new_housemate_gender": _this.new_housemate_gender,
                 "share_or_rent": _this.share_or_rent,
                 "extra_costs" : _this.extra_cost,
                 "user":_this.userid,
                 "room_costs": _this.room_costs,
                 "currency_type":_this.currency_type
             }
         };
 
         FlatsShareUserOperations.prototype.registerShareFlat = function() {
             var _this = this;
             _this.jsonData = _this.prepareShareFlatData();
             $.ajax({
                 url: _this.apiUrl,
                 method: 'PUT',
                 header: {}, contentType: 'application/json',
                 data: JSON.stringify(_this.jsonData),
                 dataType: "json",
                 success: function (response) {
                     if(response.status=="success"){
                         var flatId = response.results.id;
                         var currency_type = response.results.currency_type;
                         _this.uploadImage(flatId);
                         _this.updateRoomDeposit(flatId,currency_type);
                         $(".error-msg").html("");
                         $(".success-msg").html("Flat registered successfully");
                         $('form').each(function() { this.reset() });
                         jQuery(".cities option:gt(0)").remove();
                         jQuery('.cities').find("option:eq(0)").html("Select City");
                         $('#step1').tab('show');
                         _this.resetUploadImage();
                          localStorage.setItem("rent-flat-success", true);
                         $("#share-flat-confirm-modal-u").modal("show");
                         $('#confirm-registration-y-u').click(function () {
                             $("#share-flat-confirm-modal-u").modal("hide");
                             window.location.href ='/user/account/#user-flat';
                         });
                     }else{
                         $(".success-msg").html("");
                         $(".error-msg").html("Flat registration failed");
                     }
 
                 },
                 error: function (eResponse) {
                     $(".success-msg").html("");
                     $(".error-msg").html("Flat registration failed");
                 },complete: function (response) {
                     //
                     // $("#share-flat-confirm-modal-u").modal("show");
                     // $('#confirm-registration-y-u').click(function () {
                     //     $("#share-flat-confirm-modal-u").modal("hide");
                     //     window.location.href ='/user/account/#user-flat';
                     // });
                 }
             })
 
         };
 
         FlatsShareUserOperations.prototype.uploadImage = function(flatID) {
             var formData = new FormData();
             formData.append("flat", flatID);
             $.each($("input[type=file]"), function(i, obj) {
                 $.each(obj.files,function(j,file){
                     formData.append('flat_image', file);
                 })
             });
             $.ajax({
                 url: '/api/flat/image/',
                 type: 'POST',
                 data: formData,
                 async: false,
                 cache: false,
                 contentType: false,
                 processData: false,
                 success: function (returndata) {
                     if(returndata.status=="success"){
                         return true;
                     }else{
                         return false;
                     }
                 },
                 error: function (returndata) {
                     return false;
                 }
             });
 
         };
 
         FlatsShareUserOperations.prototype.resetUploadImage = function() {
             $(".file-input-button").css("background-image", "url('')");
             $(".file-input-button").find(".fa-times-circle").addClass("fa-plus-circle");
             $(".file-input-button").find(".fa-plus-circle").addClass("fa-plus-circle");
             $(".file-input-button").find(".fa-times-circle").removeClass("fa-times-circle");
             $(".file-input-button").find(".fa-plus-circle").removeClass("fa-times-circle");
 
         };
 
 
 
 
         FlatsShareUserOperations.prototype.updateRoomDeposit = function(flatID,currencyType) {
             var roomData = [];
             var roomDeposit = 0;
             var roomRent = 0;
             var rentInputEls = $("input[name='txt-room-rent[]']");
 
             $.each($("input[name='txt-room-deposit[]']"), function(i, obj) {
                 roomRent = rentInputEls[i].value;
                 if (obj.value) {
                     roomDeposit = obj.value;
                 } else {
                     roomDeposit = 0;
                 }
                 if (roomDeposit > 0){
                     roomData.push({share_flat: flatID, room: i + 1, deposit: roomDeposit, rent: roomRent, currency_type: currencyType});
                 }
             });
             var roomDepositData = {"deposit_details" : roomData};
             if(roomData.length > 0){
                 $.ajax({
                     url: '/api/share-flat/addroom/',
                     method: 'POST',
                     header: {}, contentType: 'application/json',
                     data: JSON.stringify(roomDepositData),
                     dataType: "json",
                     success: function (returndata) {
                         if(returndata.status=="success"){
                             return true;
                         }else{
                             return false;
                         }
                     },
                     error: function (returndata) {
                         return false;
                     }
                 });
             }
 
         };
 
 
 
 
 
 
 
 
         return FlatsShareUserOperations;
     })();
 
 
 
 
 
 
     window.FlatsShareUserOperations = FlatsShareUserOperations;
 
 }).call(this);