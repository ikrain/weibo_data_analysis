package cn.krain.weibo_data_analysis_web.web.controller;

import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import cn.krain.weibo_data_analysis_web.result.ResultUtil;
import cn.krain.weibo_data_analysis_web.service.SystemUserService;
import cn.krain.weibo_data_analysis_web.util.DataTimeUtil;
import cn.krain.weibo_data_analysis_web.util.MD5Util;
import cn.krain.weibo_data_analysis_web.util.UUIDUtil;
import com.alibaba.fastjson.JSONObject;
import com.cxytiandi.encrypt.springboot.annotation.Encrypt;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:56
 */
@Api("系统用户管理相关接口")
@Controller
@ResponseBody
@RequestMapping("/user")
public class SystemUserController {

    @Autowired
    private SystemUserService systemUserService;

    @GetMapping("/query")
    @ApiOperation("查询系统用户(参数username可以有，也可以没有)")
    public Object queryUser(String username){
        try {
            List<SystemUser> userList = systemUserService.getAllUser(username);
            JSONObject resultData = new JSONObject();
            resultData.put("userList", userList);
            return ResultUtil.success("查询成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询错误", false);
        }
    }

    /**
     * 分页查询
     * @return
     */
    @GetMapping("/queryPage")
    @ApiOperation("查询系统用户(参数username可以有，也可以没有)")
    public Object queryPageUser(String page, String limit, String username){
        try {
//            JSONObject jsonObject = JSONObject.parseObject(json);
//            String page = jsonObject.getString("page");
//            String limit = jsonObject.getString("limit");
//            String username = jsonObject.getString("username");
            Map<String, Object> map = new HashMap<>();
            //更具page和limit来计算跳跃的数字  (limit 0,3)
            int pageInt = Integer.valueOf(page);
            int limitInt = Integer.valueOf(limit);
            int skipCount = (pageInt - 1) * limitInt;
            map.put("skipCount", skipCount);
            map.put("limit", limitInt);
            map.put("username",username);
            List<SystemUser> userList = systemUserService.getAllPageUser(map);
            JSONObject resultData = new JSONObject();
            resultData.put("userList", userList);
            int total = systemUserService.queryUserNum();
            resultData.put("total", total);
            return ResultUtil.success("查询成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询错误", false);
        }
    }

    /**
     * 处理删除请求
     * @return
     */
    @GetMapping("/delete")
    @ApiOperation("根据参数id，删除指定id的系统用户")
    @ApiImplicitParam(name = "id", value = "用户id", dataType = "string")
    public Object deleteUserById(String id){
        systemUserService.delUserById(id);
        return ResultUtil.success("用户删除成功", true);
    }

    /**
     * 处理修改用户请求
     * @param json
     * @return
     */
    @PostMapping("/modify")
    @ApiOperation("根据参数id，修改指定id的系统用户")
    @ApiImplicitParams({
        @ApiImplicitParam(name = "id", value = "用户id", dataType = "string"),
        @ApiImplicitParam(name = "username", value = "用户名称", dataType = "string"),
        @ApiImplicitParam(name = "role_id", value = "用户角色id", dataType = "string")
    })
    public Object doModifyUser(@RequestBody String json){
        JSONObject jsonObject = JSONObject.parseObject(json);
        System.out.println("JSON: " + json);
        String id = jsonObject.getString("id");
        String username = jsonObject.getString("username");
        String role_id = jsonObject.getString("role_id");
        SystemUser systemUser = new SystemUser();
        systemUser.setId(id);
        systemUser.setUsername(username);
        systemUser.setRole_id(role_id);
        System.out.println("updateSysUser: " + systemUser);
        systemUserService.modifySystemUser(systemUser);
        return ResultUtil.success("用户修改成功", true);
    }

    /**
     * 处理新增用户请求
     * @param json
     * @return
     */
    @PostMapping("/add")
    @ApiOperation("根据参数id，新增一个系统用户")
    @ApiImplicitParams({
        @ApiImplicitParam(name = "username", value = "用户id", dataType = "string"),
        @ApiImplicitParam(name = "password", value = "密码", dataType = "string"),
        @ApiImplicitParam(name = "role_id", value = "用户角色id", dataType = "string"),
    })
    public Object addUser(@RequestBody String json){
        JSONObject jsonObject = JSONObject.parseObject(json);
        String username = jsonObject.getString("username");
        String password = jsonObject.getString("password");
        String role_id = jsonObject.getString("role_id");
        SystemUser systemUser = new SystemUser();
        systemUser.setId(UUIDUtil.getUUID());
        systemUser.setUsername(username);
        systemUser.setPassword(MD5Util.getMD5(password));
        systemUser.setRole_id(role_id);
        systemUser.setToken(UUIDUtil.getUUID());
        String avatar = "https://s2.loli.net/2022/05/07/KtcIQe25R9awBDj.png";
        systemUser.setAvatar(avatar);
        systemUser.setCreate_time(DataTimeUtil.getSysTime());
        systemUserService.addSystemUser(systemUser);
        return ResultUtil.success("用户添加成功", true);
    }

}
