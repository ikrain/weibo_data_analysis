package cn.krain.weibo_data_analysis_web.web.controller;

import cn.krain.weibo_data_analysis_web.entity.SystemRole;
import cn.krain.weibo_data_analysis_web.result.ResultUtil;
import cn.krain.weibo_data_analysis_web.service.SystemRoleService;
import cn.krain.weibo_data_analysis_web.util.MenuMapping;
import cn.krain.weibo_data_analysis_web.util.UUIDUtil;
import com.alibaba.fastjson.JSONObject;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.apache.commons.io.filefilter.IOFileFilter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @author cc
 * @data 2022/5/5 - 22:56
 */
@Api("系统角色管理相关接口")
@Controller
@ResponseBody
@RequestMapping("/role")
public class SystemRoleController {

    @Autowired
    private SystemRoleService systemRoleService;

    @GetMapping("/query")
    @ApiOperation("查询系统角色(参数rolename可以有，也可以没有)")
    public Object queryRole(String role_name){
        try {
            List<SystemRole> roleList = systemRoleService.getAllRole(role_name);
            JSONObject resultData = new JSONObject();
            resultData.put("roleList", roleList);
            return ResultUtil.success("查询成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询错误", false);
        }
    }

    /**
     * 处理删除角色请求
     * @return
     */
    @GetMapping("/delete")
    @ApiOperation("根据参数id，删除指定id的系统角色")
    @ApiImplicitParam(name = "id", value = "角色id", dataType = "string")
    public Object deleteRoleById(String id){
        systemRoleService.delRoleById(id);
        return ResultUtil.success("用户删除成功", true);
    }

    /**
     * 处理修改角色请求
     * @param json
     * @return
     */
    @PostMapping("/modifyAuth")
    @ApiOperation("根据参数id，修改指定id的系统角色")
    @ApiImplicitParams({
        @ApiImplicitParam(name = "menu", value = "角色权限", dataType = "string"),
        @ApiImplicitParam(name = "id", value = "角色ID", dataType = "string")
    })
    public Object doModifyRole(@RequestBody String json){
        JSONObject jsonObject = JSONObject.parseObject(json);
        String id = jsonObject.getString("id");
        String menu = jsonObject.getString("menu");
        String[] menus = menu.split("/");
        String auth = "";
        for (int i = 0; i < menus.length; i++) {
            auth += MenuMapping.MENU_VALUE.get(menus[i]);
            if (i != menus.length-1)
                auth += "/";
        }
        SystemRole systemRole = new SystemRole();
        systemRole.setId(id);
        systemRole.setMenu(auth);
        systemRoleService.modifySystemRole(systemRole);
        return ResultUtil.success("用户修改成功", true);
    }

    /**
     * 处理新增用户请求
     * @param json
     * @return
     */
    @PostMapping("/addRole")
    public Object doAddRole(@RequestBody String json){
        JSONObject jsonObject = JSONObject.parseObject(json);
        String id = UUIDUtil.getUUID();
        String rolename = jsonObject.getString("rolename");
        String represent = jsonObject.getString("represent");
        String menu = jsonObject.getString("menu");
        String[] menus = menu.split("/");
        String auth = "";
        for (int i = 0; i < menus.length; i++) {
            auth += MenuMapping.MENU_VALUE.get(menus[i]);
            if (i != menus.length-1)
                auth += "/";
        }
        SystemRole systemRole = new SystemRole();
        systemRole.setId(id);
        systemRole.setRole_name(rolename);
        systemRole.setRepresent(represent);
        systemRole.setMenu(auth);
        systemRoleService.addSystemRole(systemRole);
        return ResultUtil.success("添加角色成功", true);
    }

}
