<template>

  <div class="app">
    <navbar></navbar>

    <section class="main-content columns is-fullheight">

      <sidebar></sidebar>

      <div class="container column is-10">
        <div class="section">

          <div class="card">
            <div class="card-header"><p class="card-header-title">Header</p></div>
            <div class="card-content"><div class="content">Content</div></div>
          </div>
          <br />

          <div class="card is-hidden1">
            <div class="card-header"><p class="card-header-title">Header</p></div>
            <div class="card-content"><div class="content">Content</div></div>
          </div>
          <br />

          <div class="card is-hidden1">
            <div class="card-header"><p class="card-header-title">Header</p></div>
            <div class="card-content"><div class="content">Content</div></div>
          </div>
          <br />

          <div class="card is-hidden1">
            <div class="card-header"><p class="card-header-title">Header</p></div>
            <div class="card-content"><div class="content">Content</div></div>
          </div>
          <br />

          <div class="card is-hidden1">
            <div class="card-header"><p class="card-header-title">Header</p></div>
            <div class="card-content"><div class="content">Content</div></div>
          </div>
          <br />

          <div class="card is-hidden1">
            <div class="card-header"><p class="card-header-title">Header</p></div>
            <div class="card-content"><div class="content">Content</div></div>
          </div>
          <br />

        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Etica - Payload Delivery System'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.app {
  min-height: 100%;
  //display: flex;
  //flex-direction: column;
}
.main-content {
  //flex: 1;
}
.footer {
  margin-top: -12px;
}
@media screen and (max-width: 768px) {
  #menu-toggle:checked + .nav-menu {
    display: block;
  }
}
</style>
