import Vue from 'vue'
import VueRouter from 'vue-router'

import IndexView from '../views/IndexView.vue'

import HomeView from '../views/HomeView.vue'

import ResidentMemorySize from '../views/memory/ResidentMemorySize.vue'
import VirtualMemorySize from '../views/memory/VirtualMemorySize.vue'
import CpuLoad from '../views/process/CpuLoad.vue'
import ProcessCount from '../views/process/ProcessCount.vue'
import SMTP from '../views/email/SMTP.vue'
import POP from '../views/email/POP.vue'
import IMAP from '../views/email/IMAP.vue'
import DiskUsage from '../views/disk/diskUsage.vue'
import activeTCP from '../views/network/activeTCP.vue'
import passiveTCP from '../views/network/passiveTCP.vue'
import ThreadSnoop from '../views/process/ThreadSnoop.vue'
import tcpClose from '../views/network/tcpClose.vue'
import tcpConnLat from '../views/network/tcpConnLat'
import tcpLife from '../views/network/tcpLife'
import runQSlower from '../views/process/runQSlower'
import pidPerSec from '../views/process/pidPerSec'
import openSnoop from '../views/disk/openSnoop'

Vue.use(VueRouter)

const routes = [
  {
    show: false,
    path: '/',
    component: IndexView,
    redirect: '/home',
    children: [
      {
        path: '/home',
        name: '首页',
        component: HomeView
      }
    ]
  },
  {
    show: true,
    name: '进程信息',
    path: '/',
    component: IndexView,
    redirect: '/home',
    children: [
      {
        path: '/CpuLoad',
        name: 'CPU负载',
        component: CpuLoad
      },
      {
        path: '/ProcessCount',
        name: '进程数量',
        component: ProcessCount
      },
      {
        path: '/pidPerSec',
        name: '新建进程数量',
        component: pidPerSec
      },
      {
        path: '/ThreadSnoop',
        name: '线程创建',
        component: ThreadSnoop
      },
      {
        path: '/runQSlower',
        name: '高延迟调度',
        component: runQSlower
      }
    ]
  },
  {
    show: true,
    name: '内存信息',
    path: '/',
    component: IndexView,
    redirect: '/home',
    children: [
      {
        path: '/ResidentMemorySize',
        name: '常驻内存大小',
        component: ResidentMemorySize
      },
      {
        path: '/VirtualMemorySize',
        name: '虚拟内存大小',
        component: VirtualMemorySize        
      }
    ]
  },
  {
    show: true,
    name: '磁盘信息',
    path: '/',
    component: IndexView,
    redirect: '/home',
    children: [
      {
        path: '/DiskUsage',
        name: '磁盘空间占用',
        component: DiskUsage
      },
      {
        path: '/openSnoop',
        name: '打开文件信息',
        component: openSnoop
      }
    ]
  },
  {
    show: true,
    name: '网络信息',
    path: '/',
    component: IndexView,
    redirect: '/home',
    children: [
      {
        path: '/activeTCP',
        name: '主动TCP连接',
        component: activeTCP
      },
      {
        path: '/passiveTCP',
        name: '被动TCP连接',
        component: passiveTCP
      },
      {
        path: '/tcpConnLat',
        name: 'TCP连接延迟',
        component: tcpConnLat
      },
      {
        path: '/tcpLife',
        name: 'TCP数据大小与时长',
        component: tcpLife
      },
      {
        path: '/tcpClose',
        name: 'TCP断开连接',
        component: tcpClose
      },
      {
        path: '/SMTP',
        name: 'SMTP状态',
        component: SMTP
      },
      {
        path: '/POP',
        name: 'POP状态',
        component: POP
      },
      {
        path: '/IMAP',
        name: 'IMAP状态',
        component: IMAP
      }
    ]
  },
  // {
  //   show: true,
  //   name: '邮箱状态',
  //   path: '/',
  //   component: IndexView,
  //   redirect: '/home',
  //   children: [
  //     {
  //       path: '/SMTP',
  //       name: 'SMTP状态',
  //       component: SMTP
  //     },
  //     {
  //       path: '/POP',
  //       name: 'POP状态',
  //       component: POP
  //     },
  //     {
  //       path: '/IMAP',
  //       name: 'IMAP状态',
  //       component: IMAP
  //     }
  //   ]
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
