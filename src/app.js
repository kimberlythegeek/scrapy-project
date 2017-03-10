(function(){
  'use strict';

  angular.module('jobListings',[])
  .controller('JobsController', JobsController)
  .directive('jobsSource', jobsSource)
  .filter('excludeFilter', excludeFilter)
  .service('DataService', DataService);

  JobsController.$inject = ['$scope', 'DataService'];
  function JobsController($scope, DataService){
    var _this = this;

    // Get List of Sources from sources.json
    var promise = DataService.getSources();
    promise.then(function (response) {
      // Store in local variable
      _this.sources = response.data.sources;

      // For each source, retrieve results.
      angular.forEach(_this.sources, function(value, key) {
        var promise = DataService.getJobResults(value.file);
        promise.then(function(response) {
          // Append list of results to JSON Object
          _this.sources[key]["results"] = response.data;
        });
      });
    });
  }

  function jobsSource() {
    return {
      restrict: 'E',
      templateUrl: 'src/jobs-source.directive.html'
    };
  }


  function excludeFilter() {
    return function (input, exclude) {
      var output = [];
      angular.forEach(input, function(result) {
        if(exclude && result.title !== null) {
          if (!result.title.toLowerCase().includes(exclude)) {
            output.push(result);
          }
        } else output.push(result);
      });
      return output;
    }
  }

  DataService.$inject = ['$http'];
  function DataService($http){
    var _this = this;

    _this.getSources = function() {
      var response = $http({
        method: 'GET',
        url: ('sources.json'),
      });
      return response
    };

    _this.getJobResults = function(file) {
      var response = $http({
        method: 'GET',
        url: (file),
      });
      return response;
    };
  }

})();
