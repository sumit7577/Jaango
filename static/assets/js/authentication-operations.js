(function(){
    var AuthenticationOperations;
    AuthenticationOperations = (function(){
        AuthenticationOperations.prototype = Object.create(Main.prototype);
        var id_token = "";
        var facebook_token = "";
        var twitter_token = "";
        var twitter_token_secret = "";
        var socialMedia = false;
        var cb = new Codebird;
        var serviceName;
        function AuthenticationOperations(){
            var _this = this;
            this.events = [];
            this.init();
        }

        AuthenticationOperations.prototype.init = function () {
            var _this = this;
            _this.userCategory = $.cookie('userCategory');

            _this.googleLogin();
            //var cb = new Codebird;
            window.fbAsyncInit = function() {
                FB.init({
                    appId      : '214582072485779',
                    cookie     : true,
                    xfbml      : true,
                    version    : 'v2.8'
                });

                FB.AppEvents.logPageView();
            };

            (function(d, s, id){
                var js, fjs = d.getElementsByTagName(s)[0];
                if (d.getElementById(id)) {return;}
                js = d.createElement(s); js.id = id;
                js.src = "https://connect.facebook.net/en_US/sdk.js";
                fjs.parentNode.insertBefore(js, fjs);
            }(document, 'script', 'facebook-jssdk'));

            if(_this.userCategory == "admin"){
                if(_this.getUrlParameter("action") == "profile"){
                    _this.showAdminProfile();
                }
            }
            _this.displayUserInfoTop();

            $('#form-user-register').on('submit', function (e){
                e.preventDefault();
                if (socialMedia === true){
                    var url = '/login/';
                    var inputData = {
                        user: {
                            email: $('#email-register').val(),
                            usertype: $('[name=user-type]:checked').val()
                        },
                        first_name: $('#first-name-register').val(),
                        last_name: $('#last-name-register').val(),
                        contact_no: $('#phone-register').val(),
                        is_social_login: true,
                        google_user_id:id_token,
                        fb_user_id:facebook_token,
                        twitter_user_id:twitter_token,
                        service_name: serviceName
                    };
                    $.ajax({
                        url: url,
                        method: 'POST',
                        dataType:"json",
                        contentType: "application/json",
                        data: JSON.stringify(inputData),
                        success: function (response) {
                            LoginSuccess(response)
                            $('#register-messages').removeClass('hidden');
                            $('#reg-msg-value').text(response.message);
                        },
                        error: function (eResponse) {
                            LoginFailure(eResponse)
                        }
                    })
                } else {
                    var url = '/user/registration/';
                    var inputData = {
                        user: {
                            email: $('#email-register').val(),
                            password: $('#password-register').val(),
                            usertype: $('[name=user-type]:checked').val()
                        },
                        first_name: $('#first-name-register').val(),
                        last_name: $('#last-name-register').val(),
                        contact_no: $('#phone-register').val()
                    };
                    var data = JSON.stringify(inputData)
                    _this.checkDuplicateEmail($('#email-register').val(), data, url);
                }

            });

            $('#form-user-login').on('submit', function (e){
                e.preventDefault();
                var email = $('#email-login').val();
                var password = $('#password-login').val();
                _this.login(email,password);
            });

            $('#forgot-password').on('submit', function (e){
                e.preventDefault();
                var url = '/forgot-password/';
                var inputData = {
                    email: $('#email-forgot').val()
                };
                _this.passwordResetCall(inputData, url)
            });

            $('#logout').on('click', (e) => {
                //console.log("logout click")
                var _this = this;
                e.preventDefault();
                var url = '/logout/';
                _this.logoutCall(url)

            })


            $('#form-user-password-reset').on('submit', function (e){
                e.preventDefault();

                if( $(this).isValid() ) {
                    var restToken = _this.getUrlParameter("token");
                    var url = '/reset-password/?token='+restToken;
                    var inputData = {
                        password: $('#password').val(),
                        confirm_password: $('#confirm-password').val()
                    };
                    _this.passwordReset(inputData, url)
                }

            });

            $('#form-change-password').on('submit', function (e){
                e.preventDefault();

                if( $(this).isValid() ) {
                    var url = '/user/change_password/';
                    var inputData = {
                        password: $('#password').val(),
                        newPassword: $('#new-password').val(),
                        confirmPassword: $('#confirm-password').val()
                    };
                    _this.changePassword(inputData, url)
                }

            });

        };


        AuthenticationOperations.prototype.getUrlParameter = function(sParam) {
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

        AuthenticationOperations.prototype.showAdminProfile = function() {
            $('.nav-tabs a[href="#user-profile"]').tab('show');
            var usertype =  $.cookie('usertype');
            $('.profile-view').removeClass('hidden');
            $('.user-settings').addClass('hidden');
            if (usertype == 'individual') {
                //$('#profile-view').removeClass('hidden');
                $('#individual-info-tbl').removeClass('hidden');
                $('#individualuser-settings-form').addClass('hidden');
            }
            else {
                $('#individual-info-tbl').addClass('hidden');
                $('#individualuser-settings-form').addClass('hidden');
                $('#company-info-tbl').removeClass('hidden');
                $('#company-settings-form').addClass('hidden');
            }
        };

        AuthenticationOperations.prototype.checkDuplicateEmail = function (email, data, url) {
            var _this = this;
            var input_data = {
                email : email
            };

            $.ajax({
                url: '/registration/email/check/',
                method: 'POST',
                dataType:"json",
                contentType:"application/json",
                data: JSON.stringify(input_data),
                success: function (response) {
                    if(response.status == "success"){
                        _this.formRegisterCall(data,url);
                    }else {
                        $('#register-messages').removeClass('hidden');
                        $('#reg-msg-value').text(response.message);
                    }
                    // _this.login(inputData.user.email, inputData.user.password);
                },
                error: function (eResponse) {

                }
            })
        };

        AuthenticationOperations.prototype.formRegisterCall = function (inputData, urlData) {
            var _this = this;
            $.ajax({
                url: urlData,
                method: 'PUT',
                dataType:"json",
                contentType:"application/json",
                data: inputData,
                success: function (response) {
                    _this.RegistrationSuccess(response,inputData);
                    // _this.login(inputData.user.email, inputData.user.password);
                },
                error: function (eResponse) {
                    _this.RegistrationFailure(eResponse)
                }
            })
        };

        AuthenticationOperations.prototype.login = function (email_id,password){
            var url = '/login/';
            var inputData = {
                email: email_id,
                password: password
            };
            var data = JSON.stringify(inputData);
            this.formLoginCall(data,url);
        };

        AuthenticationOperations.prototype.RegistrationSuccess = function (successData) {
            if(successData.status == 'success'){
                $('#register-messages').removeClass('hidden');
                $('#reg-msg-value').text(successData.message);
                $('#form-user-register').find('input:text').val('');
                document.getElementById('email-register').value='';
                document.getElementById('password-register').value='';

                $('#user-individual').prop("checked", true);
            }
        };
        AuthenticationOperations.prototype.RegistrationFailure = function () {
            $('#register-error').removeClass('hidden');
        };

        AuthenticationOperations.prototype.formLoginCall = function (inputData, urlData) {
            var _this = this;
            $.ajax({
                url: urlData,
                method: 'POST',
                dataType:"json",
                contentType:"application/json",
                data: inputData,
                success: function (response) {
                    _this.LoginSuccess(response)
                },
                error: function (eResponse) {
                    _this.LoginFailure(eResponse)
                }
            })
        };

        AuthenticationOperations.prototype.LoginSuccess = function (successData) {
            var _this = this;
            //console.log("LoginSuccess",successData)
            if(successData.status == 'success'){
                if(decodeURIComponent(window.location).includes("flat/registration-form")){
                    window.location.href = '/flat/registration-form';
                }else if(decodeURIComponent(window.location).includes("rent-flat-registration/form/")){
                    window.location.href = '/rent-flat-registration/form/';
                }else{
                    window.location.href = '/user/account/';
                }

            }
            else {
                $('#login-error').removeClass('hidden');
                $('#login-error-message').text(successData.message)
                $('#form-user-login').reset

            }
        };
        AuthenticationOperations.prototype.LoginFailure = function () {
        };

        AuthenticationOperations.prototype.displayUserInfoTop = function () {
            var _this = this;
            var userId = $.cookie('userid');
            var userType = $.cookie('usertype');

            if (typeof userId !== "undefined" ) {
                _this.getUserInfo(userId);
            }

        };

        AuthenticationOperations.prototype.getUserInfo = function (userId) {
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
                    _this.renderUserInfo(response.profile_info);
                }else{
                    // User doesn't exist
                }
            });

        };

        AuthenticationOperations.prototype.renderUserInfo = function (profile_info) {
            if(profile_info.user.usertype == "individual"){
                $("#logged-in-user").html(capitaliseName(profile_info.first_name));
                $("#user-img-thumbnail").attr('src', profile_info.profile_image || '/static/assets/images/default-profile-picture.jpg');

                if($.cookie('userCategory') == "admin"){
                    $("#admin-first-name").html(capitaliseName(profile_info.first_name));
                    $("#dash-menu-view-profile").html("MANAGEMENT");
                    $("#dash-menu-view-profile-admin").removeClass("hidden");
                }else {
                    $("#first-name").html(profile_info.first_name);
                }

            }else{
                $("#first-name").html(capitaliseName(profile_info.company_name));
                $("#logged-in-user").html(capitaliseName(profile_info.company_name));
                $("#user-img-thumbnail").attr('src', profile_info.company_logo || '/static/assets/images/default-profile-picture.jpg');

            }
        };



        AuthenticationOperations.prototype.passwordResetCall = function (inputData, urlData) {
            var _this = this;
            $.ajax({
                url: urlData,
                method: 'POST',
                header:{},
                data: inputData,
                success: function (response) {
                    _this.passwordResetCallSuccess(response)
                },
                error: function (eResponse) {
                    _this.passwordResetCallFailure(eResponse)
                }
            })
        };
        AuthenticationOperations.prototype.passwordResetCallSuccess = function (successData) {
            if(successData.status == 'success'){

                $("#forgot-password-form-content").hide();
                $("#forgot-password-success-content").removeClass("hidden");

                setTimeout(function(){
                    $("#email-forgot").val("");
                    $("#forgot-password-form-content").show();
                    $("#forgot-password-success-content").addClass("hidden");
                }, 8000);
            }
        };
        AuthenticationOperations.prototype.passwordResetCallFailure = function () {
            $('#forgot-password-error').removeClass('hidden');
        };


        AuthenticationOperations.prototype.logoutCall = function (url) {
            var _this = this;
            $.ajax({
                url: url,
                method: 'GET',
                success: function (response) {
                    //console.log("logout ajax");
                    location.href='/index/';
                    _this.logoutSuccess(response)
                },
                error: function (eResponse) {
                    _this.logoutFailure(eResponse)
                }
            })
        };


        AuthenticationOperations.prototype.logoutSuccess = function () {
            location.href='/index/';
        };
        AuthenticationOperations.prototype.logoutFailure = function () {
        }


        AuthenticationOperations.prototype.logoutandReLogin = function (url) {
            var _this = this;
            $.ajax({
                url: url,
                method: 'GET',
                success: function (response) {
                    _this.logoutSuccessandRelogin(response)
                },
                error: function (eResponse) {
                    _this.logoutFailure(eResponse)
                }
            })
        };

        AuthenticationOperations.prototype.logoutSuccessandRelogin = function () {
            location.href='/index/?action=login';
        };









        AuthenticationOperations.prototype.passwordReset = function (inputData, urlData) {
            var _this = this;
            $.ajax({
                url: urlData,
                method: 'POST',
                header:{},
                data: inputData,
                success: function (response) {
                    _this.passwordResetSuccess(response)
                },
                error: function (eResponse) {
                    _this.passwordResetFailure(eResponse)
                }
            })
        };
        AuthenticationOperations.prototype.passwordResetSuccess = function (successData) {
            if(successData.status == 'success'){
                $('#reset-password-container').addClass("hidden");
                $('#password-reset-success').removeClass("hidden");
                $('#password-reset-failure').addClass("hidden");
            }else{
                $('#reset-password-container').addClass("hidden");
                $('#password-reset-success').addClass("hidden");
                $('#password-reset-failure').removeClass("hidden");
            }
        };
        AuthenticationOperations.prototype.passwordResetFailure = function () {
            $('#reset-password-container').addClass("hidden");
            $('#password-reset-success').addClass("hidden");
            $('#password-reset-failure').removeClass("hidden");
        };


        AuthenticationOperations.prototype.changePassword = function (inputData, urlData) {
            var _this = this;
            $.ajax({
                url: urlData,
                method: 'POST',
                header:{},
                data: inputData,
                success: function (response) {
                    _this.changePasswordSuccess(response)
                },
                error: function (eResponse) {
                    _this.changePasswordFailure(eResponse)
                }
            })
        };
        AuthenticationOperations.prototype.changePasswordSuccess = function (successData) {
            var _this = this;
            if(successData.status == 'success'){
                $('#change-password-success').removeClass("hidden");
                $('#change-password-error').addClass("hidden");
                setTimeout(function(){
                    var url = '/logout/';
                    _this.logoutandReLogin(url);
                }, 5000);
            }else{
                $('#change-password-error').removeClass("hidden");
                $('#change-password-success').addClass("hidden");
            }
            _this.claerChangePasswordform();
        };
        AuthenticationOperations.prototype.changePasswordFailure = function () {
            var _this = this;
            $('#change-password-error').removeClass("hidden");
            $('#change-password-success').addClass("hidden");
            _this.claerChangePasswordform();
        };
        AuthenticationOperations.prototype.claerChangePasswordform = function () {
            $('#password').val("");
            $('#new-password').val("");
            $('#confirm-password').val("");
        };


        function capitaliseName (str) {
            str = str.toLowerCase().replace(/\b[a-z]/g, function (letter) {
                return letter.toUpperCase();

            });
            return str;
        }

        var googleUser = {};
        AuthenticationOperations.prototype.googleLogin = function () {
            gapi.load('auth2', function () {
                // Retrieve the singleton for the GoogleAuth library and set up the client.
                auth2 = gapi.auth2.init({
                    client_id: '606519717766-oskathuo022vjh19tfpj9ef9hitush4q.apps.googleusercontent.com',
                    cookiepolicy: 'single_host_origin',
                    // Request scopes in addition to 'profile' and 'email'
                    //scope: 'additional_scope'
                });
                attachSignin(document.getElementById('google-sign-in-btn'));
                attachSignin(document.getElementById('google-sign-up-btn'));
            });
        };


        function loginAPI(response) {
            facebook_token = response.authResponse.accessToken;
            serviceName = "facebook"
            var url = '/login/';
            var payload = {
                is_social_login: true,
                auth_code: facebook_token,
                service_name: "facebook"
            }
            $.ajax({
                url: url,
                method: 'POST',
                dataType:"json",
                contentType: "application/json",
                data: JSON.stringify(payload),
                success: function (response) {
                    //console.log("login successfully")
                    socialMedia = true;
                    LoginSuccess(response)
                },
                error: function (eResponse) {
                    //console.log("error")
                    LoginFailure(eResponse)
                }
            })
        }

         AuthenticationOperations.prototype.checkLoginState = function (){
            FB.getLoginStatus(function(response) {
                statusChangeCallback(response);
            });
         }

        function statusChangeCallback(response) {
            //console.log('statusChangeCallback');
            //console.log(response);
            if (response.status === 'connected') {
                loginAPI(response);
            } else if (response.status === 'not_authorized') {
                document.getElementById('status').innerHTML = 'Please log '
                    + 'into this app.';
            } else {
                document.getElementById('status').innerHTML = 'Please log '
                    + 'into Facebook.';
            }
        }

        function attachSignin(element) {
            var _this = this;
            auth2.attachClickHandler(element, {},
                function (googleUser) {
                    //console.log("Signed in as: ", googleUser.getAuthResponse());
                    id_token = googleUser.getAuthResponse().id_token;
                    serviceName = "google"
                    if (id_token) {
                        var url = '/login/';
                        var payload = {
                            is_social_login: true,
                            auth_code: id_token,
                            service_name: "google"
                        }
                        $.ajax({
                            url: url,
                            method: 'POST',
                        dataType:"json",
                        contentType: "application/json",
                            data: JSON.stringify(payload),
                            success: function (response) {
                                socialMedia = true;
                            LoginSuccess(response)
                        },
                        error: function (eResponse) {
                            LoginFailure(eResponse)
                        }
                    })
                    }
                }, function(error) {
                    alert(JSON.stringify(error, undefined, 2));
                }
            );
        };


        AuthenticationOperations.prototype.getTwitterAccessToken = function() {
            cb.setConsumerKey("MCmiikfgMkB9HlzEbJ6aektTv", "hhkNAV7WlFyiX41KjGZfqHiD5IFB6Lj13lRwEpzd6JpsfG4OtY");
            cb.__call(
                "oauth_requestToken",
                {oauth_callback: "oob"},
                function (reply,rate,err) {
                    if (err) {
                        //console.log("error response or timeout exceeded" + err.error);
                    }
                    if (reply) {
                        //console.log(reply)
                        // stores it
                        cb.setToken(reply.oauth_token, reply.oauth_token_secret);
                        // gets the authorize screen URL
                        cb.__call(
                            "oauth_authorize",
                            {},
                            function (auth_url) {
                                window.codebird_auth = window.open(auth_url);
                            }
                        );
                    }
                }
            );
        }

         AuthenticationOperations.prototype.twitterPinCheck = function() {
             cb.__call(
                "oauth_accessToken",
                {oauth_verifier: document.getElementsByClassName("twitter-pinname")[0].value},
                function (reply,rate,err) {
                    //console.log(document.getElementsByClassName("twitter-pinname")[0].value)
                    //console.log(reply,rate,err)

                    if (err) {
                        //console.log("error response or timeout exceeded" + err.error);
                    }
                    if (reply) {
                        // store the authenticated token, which may be different from the request token (!)
                        cb.setToken(reply.oauth_token, reply.oauth_token_secret);
                    }

                    // if you need to persist the login after page reload,
                    // consider storing the token in a cookie or HTML5 local storage
                    twitterLoginAPI(reply);
                }
            );
        }

        function twitterLoginAPI(response) {
            twitter_token = response.oauth_token;
            twitter_token_secret = response.oauth_token_secret;
            serviceName = "twitter";
            var url = '/login/';
            var payload = {
                is_social_login: true,
                auth_code: twitter_token,
                auth_code_secret:twitter_token_secret,
                service_name: "twitter"
            }
            $.ajax({
                url: url,
                method: 'POST',
                dataType:"json",
                contentType: "application/json",
                data: JSON.stringify(payload),
                success: function (response) {
                    //console.log("login successfully")
                    socialMedia = true;
                    LoginSuccess(response)
                },
                error: function (eResponse) {
                    //console.log("error")
                    LoginFailure(eResponse)
                }
            })
        }


        function LoginSuccess(successData) {
            //console.log("LoginSuccess",successData)
            if(successData.status == 'success'){
                if(decodeURIComponent(window.location).includes("flat/registration-form")){
                    window.location.href = '/flat/registration-form';
                }else if(decodeURIComponent(window.location).includes("rent-flat-registration/form/")){
                    window.location.href = '/rent-flat-registration/form/';
                }else{
                    if (successData.user_exist === false) {
                        $('.register-modal').modal('show');
                        $('#first-name-register').val(successData.first_name);
                        $('#last-name-register').val(successData.last_name);
                        $('#email-register').val(successData.email);
                        $('#signup-password').addClass('hidden');
                        $('#password-register').removeAttr("data-validation");
                        $('.social-media-signup').addClass("hidden");

                    } else {
                        window.location.href = '/user/account/';
                    }
                }

            }
            else {
                $('#login-error').removeClass('hidden');
                $('#login-error-message').text(successData.message)
                $('#form-user-login').reset

            }
        };

        function LoginFailure(successData){

        };

        AuthenticationOperations.prototype.twitterPinSignUpCheck = function() {
            cb.__call(
                "oauth_accessToken",
                {oauth_verifier: document.getElementsByClassName("twitter-pinname")[1].value},
                function (reply,rate,err) {
                    //console.log(document.getElementsByClassName("twitter-pinname")[1].value)
                    //console.log(reply,rate,err)

                    if (err) {
                        //console.log("error response or timeout exceeded" + err.error);
                    }
                    if (reply) {
                        // store the authenticated token, which may be different from the request token (!)
                        cb.setToken(reply.oauth_token, reply.oauth_token_secret);
                    }

                    // if you need to persist the login after page reload,
                    // consider storing the token in a cookie or HTML5 local storage
                    twitterLoginAPI(reply);
                }
            );
        }

        AuthenticationOperations.prototype.getUrlParameter = function(sParam) {
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

        return AuthenticationOperations;
    })();
    window.AuthenticationOperations = AuthenticationOperations;
}).call(this);