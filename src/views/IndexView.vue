<template>
    <div class="homeBox">
        <el-container direction="vertical">
            <el-header>
                <a class="home" href="/home">HOME</a>
            </el-header>

            <el-container>
                <el-aside width="200px">
                    <el-menu router>
                        <el-submenu v-for="(route, index1) in $router.options.routes" v-if="route.show"
                            :index="index1 + ''">
                            <template slot="title">{{ route.name }}</template>
                            <el-menu-item v-for="child in route.children" :index="child.path"
                                :class="$route.path == child.path ? 'is-active' : ''">
                                {{ child.name }}
                            </el-menu-item>
                        </el-submenu>
                    </el-menu>
                </el-aside>

                <el-main>
                    <router-view></router-view>
                </el-main>
            </el-container>

            <el-footer></el-footer>
        </el-container>
    </div>
</template>

<style>
/* 容器铺满屏幕 */
html,
body,
.homeBox,
.el-container {
    margin: 0px;
    border: 0px;
    padding: 0px;
    height: 100%;
}

.home {
    color: white;
}

.el-header,
.el-footer {
    background-color: #467461;
    line-height: 60px;
}

.el-aside,
.el-submenu,
.el-menu-item {
    background-color: #ceefe1;
}

</style>
