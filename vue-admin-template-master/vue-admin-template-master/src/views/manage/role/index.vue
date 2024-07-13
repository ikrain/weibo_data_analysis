<template>
  <div class="user-card">
    <el-card>
      <div class="clearfix">
        <span class="analysis-title">角色管理</span>
        <el-form inline>
          <div class="search-input">
            <el-form-item>
              <el-input placeholder="请输入角色名" prefix-icon="el-icon-search" v-model="tempSearchObj.role_name"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="success" @click="search" style="margin-left: 5px">搜索</el-button>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" style="margin-left: 5px" @click="showAddRole">添加角色</el-button>
            </el-form-item>
          </div>
        </el-form>
      </div>

      <div>
        <el-table :data="tableData" style="width: 100%" v-loading="loading">

          <el-table-column label="序号" type="index" width="100" align="center"/>

          <el-table-column label="角色名称" width="200" align="center">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.role_name }}</span>
            </template>
          </el-table-column>

          <el-table-column label="角色权限描述" width="350" align="center">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.represent }}</span>
            </template>
          </el-table-column>

          <el-table-column label="操作" align="center">
            <template slot-scope="scope">
              <el-button size="mini" type="primary" @click="showAuth(scope.row.id, scope.row.role_name)">权限分配</el-button>
              <el-button size="mini" type="success" @click="showEditerRole(scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="delRole(scope.row.id)">删除</el-button>
            </template>
          </el-table-column>

        </el-table>
      </div>

      <!-- 权限分配对话框 -->
      <el-dialog title="权限分配" :visible.sync="dialogAuthVisible" width="500px">
        <el-tree
          :data="dataAuth"
          ref="tree"
          show-checkbox
          node-key="id"
          :default-expanded-keys="[4]"     
          :default-checked-keys="checkedArray" 
        >
        </el-tree>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel">取 消</el-button>
          <el-button :loading="loading" type="primary" @click="saveAuth()">保 存</el-button>
        </div>
      </el-dialog>

      <!-- 新增角色 对话框的结构 -->
      <el-dialog title="添加角色" :visible.sync="dialogRoleVisible">
        <el-form ref="roleForm" :model="role" label-width="120px">
          <el-form-item label="角色名">
            <el-input v-model="role.rolename"/>
          </el-form-item>

          <!-- 权限树 -->
          <el-form-item label="权限分配" class="treeAuth">
            <el-tree
              :data="dataAuth"
              ref="tree2"
              show-checkbox
              node-key="id"
              :default-expanded-keys="[4]"     
              :default-checked-keys="checkedArrayAdd" 
            >
            </el-tree>
          </el-form-item>

          <el-form-item label="角色权限描述">
            <el-input v-model="role.represent"/>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel">取 消</el-button>
          <el-button :loading="loading" type="primary" @click="saveAdd">确 定</el-button>
        </div>
      </el-dialog>
      
      <!-- 编辑角色对话框 -->
      <el-dialog title="修改角色" :visible.sync="dialogRoleEditerVisible">
        <el-form ref="roleEditerForm" :model="role" :rules="roleRules" label-width="100px">
          <el-form-item label="角色名称" prop="rolename">
            <el-input v-model="role.role_name"/>
          </el-form-item>

          <el-form-item label="角色权限描述" prop="rolename">
            <el-input v-model="role.represent"/>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel">取 消</el-button>
          <el-button :loading="loading" type="primary" @click="updateRole">确 定</el-button>
        </div>
      </el-dialog>
      <div class="bottom-page">
        <el-pagination background layout="prev, pager, next" :total="50"></el-pagination>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'Role',
  data() {
    return {
      // 表格填充数据
      tableData: [],
      // 删除所用字段
      delObj: {
        id: ''
      },

      loading: false, // 是否显示列表加载的提示
      
      // 搜索功能
      searchObj: { // 包含请求搜索条件数据的对象
        role_name: ''
      },
      tempSearchObj: { // 收集搜索条件输入的对象
        role_name: ''
      },

      // 权限管理功能
      dialogAuthVisible: false,
      checkedArray: [],// 默认勾选的数组
      dataAuth:[
        {
          id: 1,
          label: '热点话题',
        }, {
          id: 2,
          label: '情感分析',
        }, {
          id: 3,
          label: '舆情检索',
        }, {
          id: 4,
          label: '系统管理',
          children: [
            {
              id: 6,
              label: '用户管理',
            },{
              id: 7,
              label: '角色权限管理',
            }
          ]
        }, {
          id: 5,
          label: '系统配置',
        }, 
      ],
      role_auth: {},

      // 添加角色功能
      dialogRoleVisible: false, // 是否显示用户添加的dialog
      dialogRoleEditerVisible: false,// 是否显示用户修改的dialog
      // 当前要操作的role
      role: {
        rolename: '',
        represent: '',
        menu: ''
      },
      checkedArrayAdd: []
    }
  },
  // 发请求一般情况下，我们都是在mounted去发，但是也可以在created内部去发
  created() {
    this.queryRole()
  },
  methods:{
    // 查询信息（包含指定角色名称查询）
    async queryRole() {
      const { searchObj } = this
      this.loading = true
      const result = await this.$API.role.selectRole(searchObj)
      if (result.code === 200) {
        this.tableData = result.data['roleList']
      }
      this.loading = false
    },
    // 删除角色
    delRole(id) {
      this.$confirm(' 是否要删除此角色?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(async () => {
        this.delObj.id = id
        await this.$API.role.delRoleById(this.delObj)
        this.$message({
          type: 'success',
          message: '删除成功!'
        });
        this.queryRole()
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });          
      });
    },
    /* 根据输入进行搜索 */
    search() {
      this.searchObj = { ...this.tempSearchObj }
      this.queryRole()
    },
    // 显示权限分配对话框
    showAuth(id, role_name) {
      this.role_auth.id = id
      this.searchObj.role_name = role_name
      this.$API.role.selectRole(this.searchObj).then((result) => {
        var str = result.data["roleList"][0].menu
        var menu = []
        menu = str.split("/")
        this.checkedArray = []
        for(var i=0; i<menu.length; i++){
          if( menu[i] == 'Topic' ){
            this.checkedArray[0] = 1
          }else if( menu[i] == 'Emotion' ){
            this.checkedArray[1] = 2
          }else if( menu[i] == 'Search' ){
            this.checkedArray[2] = 3
          }
          // else if( menu[i] == 'Manage' ){
          //   this.checkedArray[3] = 4
          // }
          else if( menu[i] == 'Set' ){
            this.checkedArray[4] = 5
          }else if( menu[i] == 'User' ){
            this.checkedArray[5] = 6
          }else if( menu[i] == 'Role' ){
            this.checkedArray[6] = 7
          }
        }
        this.dialogAuthVisible = true
        this.searchObj.role_name = ''
      })
      // this.dialogAuthVisible = true
    },
    // 保存权限更改
    saveAuth(role_id) {
      var parentIds = this.$refs.tree.getHalfCheckedNodes()
      var childsIds = this.$refs.tree.getCheckedNodes()
      // const nodes = this.$refs.tree.getCheckedNodes(true)
      const nodes = parentIds.concat(childsIds)
      var menu = ''
      for(var i=0; i<nodes.length; i++){
        menu = menu + nodes[i].label
        if(i !== nodes.length-1)
          menu = menu + '/'
      }
      this.role_auth.menu = menu
      this.$API.role.updateRoleAuth(this.role_auth).then((result) => {
        this.loading = false
        this.$message.success('修改权限成功!')
        this.queryRole()
        this.role_auth = {}
        this.dialogAuthVisible = false
      })
    },
    // 权限取消保存按钮
    cancel() {
      this.checkedArray = []
      this.dialogAuthVisible = false
    },
    // 弹出新增用户对话框
    showAddRole(){
      this.dialogRoleVisible = true;
      this.$nextTick(() => this.$refs.roleForm.clearValidate());
    },

    // 弹出编辑用户对话框
    showEditerRole(role){
      this.role = role
      this.dialogRoleEditerVisible = true;
      //this.$nextTick(() => this.$refs.userForm.clearValidate())
    },

    // 保存新增能按钮
    saveAdd(){
      var parentIds = this.$refs.tree2.getHalfCheckedNodes()
      var childsIds = this.$refs.tree2.getCheckedNodes()
      const nodes = parentIds.concat(childsIds)
      var menu = ''
      for(var i=0; i<nodes.length; i++){
        menu = menu + nodes[i].label
        if(i !== nodes.length-1)
          menu = menu + '/'
      }
      this.role.menu = menu
      console.log(this.role)
      this.$API.role.addRole(this.role).then((result) => {
        this.loading = false
        this.$message.success('添加角色成功!')
        this.role = {}
        this.dialogRoleVisible = false
      })
      this.queryRole()
    },

    // 更新角色名称和描述
    updateRole(){
      console.log(this.role);
    }
  }
}
</script>

<style scoped>
.search-input {
  width: 370px;
  cursor: pointer;
}

.clearfix .search-input {
  display: flex;
  justify-content: space-between;
}

.clearfix {
  border-bottom: 1px solid #eee;
}

.analysis-title {
  font-family: "Microsoft YaHei";
  font-size: 22px;
  line-height: 50px;
}

.bottom-page {
  padding-top: 10px;
}

.user-card{
  margin-top: 10px;
}

.el-tree{
  padding-left: 150px;
  border: 1px solid #c0c1c3;
}

</style>
