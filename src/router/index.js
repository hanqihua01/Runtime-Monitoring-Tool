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
import FaultDiagnosisFind from '../views/FaultDiagnosis/FaultDiagnosisFind.vue'
import TCP from '../views/network/TCP.vue'

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
        path: '/TCP',
        name: 'TCP连接信息',
        component: TCP
      }
    ]
  },
  {
    show: true,
    name: '邮箱状态',
    path: '/',
    component: IndexView,
    redirect: '/home',
    children: [
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
  {
    show: true,
    name: '故障诊断',
    path: '/',
    component: IndexView,
    redirect: '/home',
    children: [
      {
        path: '/FaultDiagnosisFind',
        name: '故障日志定位',
        component: FaultDiagnosisFind
      }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
