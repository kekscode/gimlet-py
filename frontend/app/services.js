/**
* Encapsulates a RESTful service for our app
*/

angular.module('AppServices', ['ngResource'])
  .factory('GimletArticles', function($resource){
    return $resource('http://127.0.0.1:9090/api/v1/blog/articles', {})
  })
  .value('version', '0.1');
