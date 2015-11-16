/**
 * AngularJS App for Gimlet Blog API
 */

'use strict';

// Create our Sitesitter Exif Viewer application object
var App = angular.module('App', [
    'ngRoute',
    'AppControllers',
]);

// Configure App
App.config(['$routeProvider', '$locationProvider',
    function ($routeProvider, $locationProvider) {
        $routeProvider.
            when('/', {
                templateUrl: 'partials/main.html',
                controller: 'MainCtrl'
            });
        $locationProvider.html5Mode(false).hashPrefix('#');
    }]);
