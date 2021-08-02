/**
 * ajax request model
 */
 "use strict";
 (function(){
     var AjaxRequestModel;
     AjaxRequestModel= (function(){
         AjaxRequestModel.prototype = Object.create(Main.prototype);
 
         function AjaxRequestModel(){
             var _this= this;
             this.events = [];
         }
         AjaxRequestModel.prototype.init = function () {
             var _this= this;
         };
         AjaxRequestModel.prototype.ajaxRequestModelFunction = function(instance,requestType,url,inputData,sFunction,eFunction,message){
 
             var _this= this;
             
             $.ajax({
                 type: requestType,
                 url: url,
                 cache: false,
                 data: inputData,
                 dataType: 'json',
                 headers: {"Content-Type": "application/json",
                     "Accept":"application/json"},
                 success: function(data){
                     instance.dispatchit(sFunction,[data]);
                 },
                 error: function(data){
                     instance.dispatchit(eFunction,[data]);
                 }
             });
         };
         return AjaxRequestModel;
     })();
     window.AjaxRequestModel= AjaxRequestModel;
 }).call(this);