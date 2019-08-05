<template>
      <aside class="column is-2 is-narrow-mobile is-fullheight section is-hidden-mobile" style="padding-left: 35px;">
        <p class="menu-label is-hidden-touch">Navigation</p>
        <ul class="menu-list">
          <li>
            <a href="#" class="">
              <span class="icon"><i class="fa fa-home"></i></span> Home
            </a>
          </li>
          <li>
            <a href="#" class="is-active">
              <span class="icon"><i class="fa fa-table"></i></span> Links
            </a>

            <ul>
              <li>
                <a href="#">
                  <span class="icon is-small"><i class="fa fa-link"></i></span> Link1
                </a>
              </li>
              <li>
                <a href="#">
                  <span class="icon is-small"><i class="fa fa-link"></i></span> Link2
                </a>
              </li>
            </ul>
          </li>
          <li>
            <a href="#" class="">
              <span class="icon"><i class="fa fa-info"></i></span> About
            </a>
          </li>
        </ul>
      </aside>
</template>

<script>
export default {
  data () {
    return {
      sidebar: 'Testing Sidebar'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
