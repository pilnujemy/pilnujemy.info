var fs = require('fs');
var gulp = require('gulp');
var gulpp = require('gulp-load-plugins')();
var json = JSON.parse(fs.readFileSync("./package.json"));


var config = (function () {
    var root = './theme';

    var path = {
        root: root,
        bower: "./bower_components/",
        assets: root + "/assets",
        static: root + "/static"
    };

    return {
        path: path,
        html: {
            input: path.root + "/templates/*.html",
            watch: path.root + "/templates/*.html",
        },
        scss: {
            input: path.assets + "/scss/*.scss",
            include: [
                path.assets + "/scss/"
            ],
            output: path.static + "/css",
            watch: [
                path.assets + "/scss/**.scss"
            ]
        },
        script: {
            input: [
                // path.bower + "/jquery/dist/jquery.js",
                // path.bower + "/bootstrap-sass/assets/javascripts/bootstrap.js",
                path.assets + "/js/*.js"
            ],
            output: {
                dir: path.static + "/js/",
                filename: "script.js"
            },
            watch: [
                path.assets + "/js/*.js"
            ]
        },
        images: {
            input: path.assets + "/images/*",
            output: path.static + "/images/"
        }
    };
}());

gulp.task("html", function () {
    return gulp.src(config.html.input)
        .pipe(gulpp.livereload());
});

gulp.task("scss", function () {
    return gulpp.rubySass(
        config.scss.input,
        {
            style: "expanded",
            loadPath: config.scss.include,
            sourcemap: false
        }
    )
        .pipe(gulpp.autoprefixer("last 1 version", "> 1%", "ie 8", "ie 7"))
        .pipe(gulp.dest(config.scss.output))
        .pipe(gulpp.livereload())
        .pipe(gulpp.rename({extname: ".min.css"}))
        .pipe(gulpp.minifyCss())
        .pipe(gulp.dest(config.scss.output))
        .pipe(gulpp.livereload());
});

gulp.task("js", function () {
    return gulp.src(config.script.input)
        .pipe(gulpp.concat(config.script.output.filename))
        .pipe(gulp.dest(config.script.output.dir))
        .pipe(gulpp.livereload())
        .pipe(gulpp.uglify())
        .pipe(gulpp.rename({extname: ".min.js"}))
        .pipe(gulp.dest(config.script.output.dir))
        .pipe(gulpp.livereload());
});

gulp.task("images", function () {
    return gulp.src(config.images.input)
        .pipe(gulpp.imagemin())
        .pipe(gulp.dest(config.images.output));
});

gulp.task("watch", function(){
    gulp.watch(config.html.watch, ["html"]);
    gulp.watch(config.scss.watch, ["scss"]);
    gulp.watch(config.script.watch, ["js"]);
});

gulp.task("build", ["scss", "js", "images"]);
gulp.task("default", ["build", "watch"]);
