'use strict';

var autoprefix = require("gulp-autoprefixer"),
  connect = require("gulp-connect"),
  gulp = require("gulp"),
  bourbon = require("bourbon").includePaths,
  neat = require("bourbon-neat").includePaths,
  sass = require("gulp-sass");

// Watch the scss paths.
var paths = {
  scss: ["./frontend/src/assets/scss/*.scss"]
};

gulp.task("sass", function() {
  return gulp.src(paths.scss)
    .pipe(sass({
      sourceMaps: true,
      includePaths: [bourbon, neat]
    }))
    .pipe(gulp.dest("./codingartist/codingartist/static/css"))
});

gulp.task("connect", function() {
  connect.server({
    root: "web",
    port: 8081,
    livereload: true
  });
});

gulp.task("default", ["sass"], function() {
  gulp.watch(paths.scss, ["sass"]);
})