<template>
  <el-row :gutter="10">
    <el-col :xs="14" :sm="10" :md="7" :lg="6" :xl="6">
      <el-menu default-active="1" class="toi-header-nav" mode="horizontal">
        <el-menu-item index="1" @click="$router.push('/')">ホーム</el-menu-item>
        <el-menu-item index="2" @click="$router.push('/notification')">通知</el-menu-item>
        <el-menu-item index="3" @click="$router.push('/message')">メッセージ</el-menu-item>
      </el-menu>
    </el-col>
    <el-col
        :xs="{span:0, offset:1}"
        :sm="{span:5, offset:3}"
        :md="{span:5, offset:7}"
        :lg="{span:5, offset:9}"
        :xl="{span:5, offset:9}">
      <el-input
        placeholder="検索"
        prefix-icon="el-icon-search">
      </el-input>
    </el-col>
    <el-col :xs="9" :sm="6" :md="5" :lg="4" :xl="4">
      <el-button type="primary" icon="el-icon-edit" circle></el-button>
      <el-button type="primary" round>ツイート</el-button>
    </el-col>
  </el-row>
</template>

<style>
.toi-header-nav {
  width: 270px;
}

.el-input {
  margin-top: 10px;
}

.el-button {
  margin-top: 10px;
}

.el-row {
  border-bottom: solid 1px #ebebeb;
}

</style>