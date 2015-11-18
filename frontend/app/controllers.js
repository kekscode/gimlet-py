/**
* Controllers for our app
*/

'use strict';

var AppControllers = angular.module('AppControllers', []);

AppControllers.controller('MainCtrl', function ($scope, $http, cfg) {

  console.log("controller MainCtrl called");
  console.log(cfg);

  // Instantiate an object to store your scope data in (a good practice)
  $scope.data = {};

  $http.get(cfg.articlesResource).then(function(response){
    console.log("success" + response);
    $scope.data.articles = response.data;
  }, function(response){
    console.log("fail!" + response)
  });
});
