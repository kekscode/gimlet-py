/**
* Controllers for our app
*/

'use strict';

var AppControllers = angular.module('AppControllers', []);

AppControllers.controller('MainCtrl', function ($scope, $location, $http, $window, cfg) {

  console.log("controller MainCtrl called");
  console.log(cfg);

  // Instantiate objects to store your scope data in (a good practice)
  $scope.data = {};
  $scope.functions = {};

  // Fetch and display all articles
  $http.get(cfg.listArticlesResource)
    .then(function(response){
      console.log("success" + response);
      $scope.data.articles = response.data;
    }, function(response){
      console.log("fail!" + response)
    });

    // Delete article by ID
    $scope.functions.deleteArticle = function(articleID) {
      $http.delete(cfg.articleResource + "/" + articleID)
        .then(function(response){
          console.log("success" + response);
          $window.location.reload(); // TODO: Omit full reload somehow
        }, function(response){
          console.log("fail!" + response)
        });
    }
});

AppControllers.controller('NewArticleCtrl', function($scope, $http, cfg) {
  console.log("controller NewArticleCtrl called");

  $scope.data = {}

});
