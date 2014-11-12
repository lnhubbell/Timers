'use strict';

// Declare app level module which depends on views, and components
var api = angular.module('myApp', ['ngResource']);

api.config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

// Service
api.factory('Timer', [
  '$resource', function($resource) {
    var resourceObj = $resource('https://stark-hamlet-6905.herokuapp.com/timers/:id/', 
    {id: '@id'},
    {update: {
        method: 'PUT' // this method issues a PUT request
      },
    });
    return resourceObj
  }
]);

// Controllers
api.controller('timersController', [
    '$scope', 'Timer', function($scope, Timer) {
    $scope.runningTimers = [];
    $scope.timers = [];
    $scope.newTimer = new Timer();

    $scope.updateTimer = function(timerObj) {
        Timer.get(timerObj, function(timer) {
            timer.seconds = Math.round(timerObj.seconds);
            timer.$update();
        })
    };

    $scope.deleteTimer = function(timerObj, index) {
        Timer.get({id: timerObj.id}, function(timer) {
            timer.$remove().then(function() {
                var length = $scope.timers.length;
                var before = $scope.timers.slice(0, index);
                var after = $scope.timers.slice(index+1, length)
                $scope.timers = before.concat(after);
            });
        })

    };

    $scope.addTimer = function(name) {
        var timerObj = {name: name, seconds: 0};
        $scope.saveTimer(timerObj);
    };

    $scope.saveTimer = function(timerObj) {
        $scope.newTimer.name = timerObj.name;
        $scope.newTimer.seconds = timerObj.seconds;
        return $scope.newTimer.$save().then(function(result) {
          return $scope.timers.push(result);
        }).then(function() {
          return $scope.newTimer = new Timer();
        }).then(function() {
            $scope.name = null;
          return $scope.errors = null;
        }, function(rejection) {
          return $scope.errors = rejection.data;
        });
    };

    $scope.startTimer = function(timer, index) {
        // intitial variables
        var setPoint = $scope.timers[index].seconds,
            start = new Date().getTime(),
            elapsed = '0.00';
        // timer loop
        var interval = window.setInterval(function()
        {
            var time = new Date().getTime() - start;
            elapsed = Math.floor(time / 100) / 10;
            var newTime = Number(setPoint) + Number(elapsed);
            for (var i = 0; i < $scope.timers.length; i++) {
                if ($scope.timers[i].id === timer.id) {
                    $scope.timers[i].seconds = newTime.toFixed(0);
                }
            }
            $scope.$apply();
        }, 100);
        // add timer id to list of running timers
        for (var i = 0; i < $scope.timers.length; i++) {
            if ($scope.timers[i].id === timer.id) {
                $scope.runningTimers[timer.id] = interval;
            }
        };
    };

    $scope.stopTimer = function(timer, index) {
        window.clearInterval($scope.runningTimers[timer.id]);
        $scope.runningTimers[timer.id] = null;
        $scope.updateTimer(timer);
    };
  }
]);

api.controller('resourceController', [
  '$scope', '$http', function($scope, $http) {
    return $http.get('https://stark-hamlet-6905.herokuapp.com/timers/?format=json').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.timers.push(item);
      });
    });
  }
]);


