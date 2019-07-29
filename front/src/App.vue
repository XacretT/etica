<template>
  <div id="app">
    <img src="./assets/logo-circular.svg"
    alt="Etica - Payload Delivery System"
    height="125px"
    width="125px" >
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
$primary-dark-background: #1e1e2f;

$primary-yellow-light: #F6F01B;
$primary-yellow-dark: #F9D417;
$primary-gradient-light: #87157C;
$primary-gradient-dark: #130742;

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
$body-color: $white;

//Typography
@import url('https://fonts.googleapis.com/css?family=Montserrat&display=swap');
$family-serif: 'Montserrat', 'Helvetica', 'serif';
$family-primary: $family-serif;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";

</style>
