<template>
  <div id="app">
    <el-container>
    <el-header>
      <header-view/>
      </el-header>
      <el-main>
      <router-view/>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import "element-ui/lib/theme-chalk/index.css"
  import HeaderView from '@/components/Header'

  export default {
    components: {
      HeaderView
    },
  }
</script>
