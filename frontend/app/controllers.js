/**
* Controllers for our app
*/

'use strict';

var AppControllers = angular.module('AppControllers', []);

AppControllers.controller('MainCtrl', function ($scope, GimletArticles) {
  console.log("controller MainCtrl called");

  // Instantiate an object to store your scope data in (a good practice)
  $scope.data = {};

  GimletArticles.query(function(response) {
    // Assign the response INSIDE the callback
    $scope.data.articles = response;
});
});
