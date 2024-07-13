<template>
  <div class="user-card">
    <el-card>
      <!-- 顶部title和搜索框 -->
      <div class="clearfix">
        <span class="analysis-title">用户管理</span>
        <el-form inline>
          <div class="search-input">
            <el-form-item>
              <el-input placeholder="请输入用户名" prefix-icon="el-icon-search" v-model="tempSearchObj.username"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="success" @click="search" style="margin-left: 5px">搜索</el-button>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" style="margin-left: 5px" @click="showAddUser">添加账户</el-button>
            </el-form-item>
          </div>
        </el-form>
      </div>
      <!-- 表格 -->
      <div>
        <el-table :data="tableData" style="width: 100%" v-loading="loading">

          <el-table-column label="序号" type="index" width="100" align="center"/>

          <el-table-column label="用户名" width="200" align="center">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.username }}</span>
            </template>
          </el-table-column>

          <el-table-column label="用户角色" width="200" align="center">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.role_name }}</span>
            </template>
          </el-table-column>

          <el-table-column label="账号创建时间" width="200" align="center">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 10px">{{ scope.row.create_time }}</span>
            </template>
          </el-table-column>

          <el-table-column label="操作" align="center">
            <template slot-scope="scope">
              <el-button size="mini" type="success" @click="showEditerUser(scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="delUser(scope.row.id)">删除</el-button>
            </template>
          </el-table-column>

        </el-table>
      </div>
      <!-- 新增用户 对话框的结构 -->
      <el-dialog title="添加用户" :visible.sync="dialogUserVisible">
        <el-form ref="userForm" :model="user" :rules="userRules" label-width="100px">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="user.username"/>
          </el-form-item>
          
          <el-form-item v-if="!user.id" label="用户密码" prop="password">
            <el-input v-model="user.password"/>
          </el-form-item>

          <el-form-item v-if="!user.id" label="用户角色" prop="rolename">
            <el-radio-group v-model="user.role_id">
              <el-radio v-for="item in this.roleList" :key="item.role_name" :label="item.id">{{item.role_name}}</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel">取 消</el-button>
          <el-button :loading="loading" type="primary" @click="add">确 定</el-button>
        </div>
      </el-dialog>
      <!-- 编辑用户对话框 -->
      <el-dialog title="修改用户" :visible.sync="dialogUserEditerVisible">
        <el-form ref="userEditerForm" :model="user" :rules="userRules" label-width="100px">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="user.username"/>
          </el-form-item>

          <el-form-item label="用户角色" prop="rolename">
            <el-radio-group v-model="user.role_id">
              <el-radio v-for="item in this.roleList" :key="item.id" :label="item.id">{{item.role_name}}</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancel">取 消</el-button>
          <el-button :loading="loading" type="primary" @click="update">确 定</el-button>
        </div>
      </el-dialog>
      <!-- 分页器 -->
      <div class="bottom-page">
        <el-pagination
          :current-page="this.searchObj.page"
          :total="total"
          :page-size="limit"
          :page-sizes="[5, 10, 15]"
          style="padding: 20px 0;"
          layout="prev, pager, next, jumper, ->, sizes, total"
          @current-change="getUsers"
          @size-change="handleSizeChange"
        />
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'User',
  data() {
    return {
      // 表格填充数据
      tableData: [],
      // 删除所用字段
      delObj: {
        id: ''
      },
      listLoading: false, // 是否显示列表加载的提示
      searchObj: { // 包含请求搜索条件数据的对象
        username: '',
        // 实现分页的字段
        page: 1,
        limit: 7
      },
      tempSearchObj: { // 收集搜索条件输入的对象
        username: '',
        page: 1,
        limit: 7
      },
      dialogUserVisible: false, // 是否显示用户添加的dialog
      dialogUserEditerVisible: false,// 是否显示用户修改的dialog
      user: {}, // 当前要操作的user
      userRules: { // 用户添加/修改表单的校验规则
        username: [
          { required: true, message: '用户名必须输入' },
          { min: 4, message: '用户名不能小于4位' }
        ],
        password: [
          { required: true, validator: this.validatePassword }
        ]
      },
      roleList: [],// 记录所获取的所有角色列表

      selectedIds: [], // 所有选择的user的id的数组
      users: [], // 当前页的用户列表
      loading: false, // 是否正在提交请求中
      allRoles: [], // 所有角色列表
      userRoleIds: [], // 用户的角色ID的列表
      isIndeterminate: false, // 是否是不确定的
      checkAll: false // 是否全选
    }
  },

  // 发请求一般情况下，我们都是在mounted去发，但是也可以在created内部去发
  created() {
    // this.queryUser()
    this.getUsers()
  },

  methods: {
    // 查询信息（包含指定用户名称查询）
    // async queryUser() {
    //   const { searchObj } = this
    //   const result = await this.$API.user.selectUser(searchObj)
    //   if (result.code === 200) {
    //     this.tableData = result.data['userList']
    //   }
    // },
    // 删除用户
    delUser(id) {
      this.$confirm(' 是否要删除此用户?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(async () => {
        this.delObj.id = id
        await this.$API.user.delUserById(this.delObj)
        this.$message({
          type: 'success',
          message: '删除成功!'
        });
        this.getUsers()
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });          
      });
    },

    /*
    根据输入进行搜索
    */
    search() {
      this.searchObj = { ...this.tempSearchObj }
      this.getUsers()
    },

    // 异步获取角色列表
    async getRoles(){
      const reslut = await this.$API.role.selectRole();
      this.roleList = reslut.data["roleList"];
    },

    // 弹出新增用户对话框
    showAddUser(){
      this.user = {};
      this.getRoles();
      this.dialogUserVisible = true;
      this.$nextTick(() => this.$refs.userForm.clearValidate());
      this.getUsers();
    },

    // 弹出编辑用户对话框
    showEditerUser(user){
      this.user = user
      this.getRoles();
      this.dialogUserEditerVisible = true;
      // this.$nextTick(() => this.$refs.userForm.clearValidate())
    },

    update(){
      this.loading = true
      this.$API.user.updateUser(this.user).then((result) => {
        this.loading = false
        this.$message.success('修改成功!')
        this.getUsers()
        this.user = {}
        this.dialogUserEditerVisible = false
      })
    },

    add(){
      this.$refs.userForm.validate(valid => {
        if (valid) {
          const {user} = this
          this.loading = true
          this.$API.user.insertUser(user).then((result) => {
            this.loading = false
            this.$message.success('添加成功!')
            this.getUsers()
            this.user = {}
            this.dialogUserVisible = false
          })
        }
      })
    },

    /* 获取分页列表 */
    async getUsers(page = 1) {
      this.searchObj.page = page
      const { limit, searchObj } = this
      this.loading = true
      const result = await this.$API.user.getPageList(searchObj)
      this.loading = false
      this.tableData = result.data["userList"]
      this.total = result.data["total"]
    },

    /* 处理pageSize发生改变的监听回调 */
    handleSizeChange(pageSize) {
      this.searchObj.page = 1
      this.searchObj.limit = pageSize
      this.getUsers()
    },
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

.user-card {
  margin-top: 10px;
}
</style>
