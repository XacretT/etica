<template>
    <nav class="navbar nav is-transparent is-fixed-top">
      <div class="navbar-brand">
        <a class="navbar-item E-button" id="E-button" href="/">
          <img style="padding-left: 10px" src="../assets/logo.svg"
          alt="Etica - Payload Delivery System"
          height="45px"
          width="45px"/>
        </a>
      </div>
      <div class="navbar-item">
        <h1 class="title is-3">{{title}}</h1>
      </div>
    </nav>
</template>

<script>
export default {
  data () {
    return {
      title: 'Etica Payload Delivery System'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.navbar {
  padding: 10px 0px 0px 0px;
}
</style>
