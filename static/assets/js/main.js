"use strict";
(function () {
    var Main;
    Main = (function () {
        Main.prototype.events = [];
        function Main(params) {
        }

        Main.prototype.initMain = function(){
        };

        Main.prototype.getValueFromId = function(elementId){
            return document.getElementById(elementId).value;
        };

        Main.prototype.addEventlistener = function (event, callback) {
            this.events[event] = this.events[event] || [];
            if (this.events[event]) {
                this.events[event].push(callback);
            }
        };

        Main.prototype.removeEventlistener = function (event, callback) {
            if (this.events[event]) {
                var listeners = this.events[event];
                for (var i = listeners.length - 1; i >= 0; --i) {
                    if (listeners[i] === callback) {
                        listeners.splice(i, 1);
                        return true;
                    }
                }
            }
            return false;
        };

        Main.prototype.dispatchit = function (event, args) {
            if (this.events[event]) {
                var listeners = this.events[event], len = listeners.length;
                while (len--) {
                    listeners[len].apply(this, args);
                }
            }
        };
        return Main;

    })();

    window.Main = Main;

        $.fn.isInViewport = function() {
          var elementTop = $(this).offset().top;
          var elementBottom = elementTop + $(this).outerHeight();

          var viewportTop = $(window).scrollTop();
          var viewportBottom = viewportTop + $(window).height();

          return elementBottom > viewportTop && elementTop < viewportBottom;
        };

        $(window).on('scroll', function() {
            if ($('.footer-bottom-row').isInViewport()) {
                $('.footer-wrapper').removeClass('stick-bottom');
            } else {
                if($(this).scrollTop() === 0){
                    $('.footer-wrapper').removeClass('stick-bottom');
                    return;
                }
                $('.footer-wrapper').addClass('stick-bottom');
            }
        });

}).call(this);
