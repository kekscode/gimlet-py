/**
* Controllers for our app
*/

'use strict';

var AppControllers = angular.module('AppControllers', []);

AppControllers.controller('MainCtrl', function ($scope, $route, $location, $http, cfg) {
  // Instantiate objects to store your scope data in (a good practice)
  $scope.data = {};
  $scope.functions = {};

  // Fetch and display all articles
  $http.get(cfg.listArticlesResource)
  .then(function(response){
    $scope.data.articles = response.data;
  }, function(response){
    console.log("fail!" + response)
  });

  // Delete article by ID
  $scope.functions.deleteArticle = function(articleID) {
    $http.delete(cfg.articleResource + "/" + articleID)
    .then(function(response){
      $route.reload(); // reload articles
    }, function(response){
      console.log("fail!" + response)
    });
  }
});

AppControllers.controller('NewArticleCtrl', function($scope, $route, $http, cfg) {
  $scope.functions = {};
  $scope.functions.createArticle = function(articleID) {
    $scope.blogpost = {};

    $scope.blogpost.title = $scope.title;
    $scope.blogpost.subtitle = $scope.subtitle;
    $scope.blogpost.body = $scope.body;

    $http.post(cfg.articleResource + "/create", $scope.blogpost)
    .then(function(response) {
      $route.reload()
    }, function(response){
      console.log("fail!" + response)
    });
  }
});
