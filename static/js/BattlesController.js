'use strict';

var app = angular.module('GOTBattles', ['ngSanitize',
    'ui.bootstrap'
]);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

app.controller(
    'GotBattlesController', [
        '$scope',
        '$http',
        function($scope, $http) {
            $scope.getAllBattles = function() {
                $scope.search_result = null;
                $scope.battlesStatics = null;
                $scope.searchEnable = false;
                $scope.showInputError = false;
                $scope.all_battles_formatted = "Loading All Battles Data..."

                $http({
                    url: "/count",
                    method: "GET",
                    withCredentials: true
                }).success(function(data, status) {
                    $scope.battles_count = data.count;
                }).error(function(data, status) {
                    $scope.battles_count = null;
                });

                $http({
                    url: "/list",
                    method: "GET",
                    withCredentials: true
                }).success(function(data, status) {
                    $scope.all_battles_formatted = $scope.formatJson(angular.toJson(data.result,
                        4));
                }).error(function(data, status) {
                    $scope.all_battles_formatted = "Loading error"
                });
            }

            $scope.getStatics = function() {
                $scope.search_result = null;
                $scope.searchEnable = false;
                $scope.showInputError = false;
                $scope.all_battles_formatted = null;
                $scope.battles_count = null;
                $scope.battlesStatics = "Loading..."
                $http({
                    url: "/stats",
                    method: "GET",
                    withCredentials: true
                }).success(function(data, status) {
                    $scope.battlesStatics = $scope.formatJson(angular.toJson(data.result,
                        4));
                }).error(function(data, status) {
                    $scope.battlesStatics = "Lading error"
                });
            }

            $scope.showSearchs = function() {
                $scope.battlesStatics = null;
                $scope.all_battles_formatted = null;
                $scope.battles_count = null;
                $scope.searchEnable = true;
                $scope.showInputError = false;
                $scope.search_result = null;
            }

            $scope.search = function() {
                $scope.search_result = "Searching...."
                $http({
                    url: "/search?"+ "name=" + $scope.name + "&attacker_king=" + $scope.attacker_king +"&defender_king="+$scope.defender_king +"&battle_type="+$scope.battle_type + "&location="+$scope.location,
                    method: "GET",
                    withCredentials: true,
                }).success(function(data, status) {
                    $scope.search_result = $scope.formatJson(angular.toJson(data.result,
                        4));
                }).error(function(data, status) {
                    $scope.search_result = "Search Error"
                });


            }


            $scope.formatJson = function(json) {
                json = json.replace(/&/g, '&amp;').replace(
                    /</g, '&lt;').replace(/>/g, '&gt;');
                return json
                    .replace(
                        /("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g,
                        function(match) {
                            var cls = 'number';
                            if (/^"/.test(match)) {
                                if (/:$/.test(match)) {
                                    cls = 'key';
                                } else {
                                    cls = 'string';
                                }
                            } else if (/true|false/
                                .test(match)) {
                                cls = 'boolean';
                            } else if (/null/
                                .test(match)) {
                                cls = 'null';
                            }
                            return '<span class="' +
                                cls + '">' +
                                match + '</span>';
                        });
            }
        }
    ]);