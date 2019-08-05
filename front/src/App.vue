<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="scss">
// Import Bulma's core
@import "~bulma/sass/utilities/_all";

// Defining main theme colors
$primary-light-background: #27293d;
$primary-dark-background: #1e1e2e;

$primary-yellow-light: #F6F01B;
$primary-yellow-dark: #F9D417;
$primary-gradient-light: #87157C;
$primary-gradient-dark: #130742;

$primary-text-color: hsla(0,0%,100%,.8);
$primary: $primary-yellow-light;
$primary-invert: findColorInvert($primary);

// Setup $colors to use as bulma classes (e.g. 'is-white')
$colors: (
    "white": ($white, $black),
    "black": ($black, $white),
    "light": ($light, $light-invert),
    "dark": ($dark, $dark-invert),
    "primary": ($primary, $primary-invert),
    "info": ($info, $info-invert),
    "success": ($success, $success-invert),
    "warning": ($warning, $warning-invert),
    "danger": ($danger, $danger-invert),
);

// Links
$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;
$link-hover: $primary-yellow-dark;

//Body styles
$body-background-color: $primary-dark-background;
$body-color: $primary-text-color;
$navbar-background-color: none;
$navbar-item-color: $primary-text-color;
$navbar-item-img-max-height: 3.5rem !important;
$navbar-height: 4rem !important;
$navbar-padding-vertical: 2rem;

//Typography
$family-serif: 'BlinkMacSystemFont','-apple-system','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Fira Sans','Droid Sans','Helvetica Neue','Helvetica','Arial','sans-serif';
$family-primary: $family-serif;
$title-color: $primary-text-color !default;
$title-weight: $weight-light !important;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";

</style>
