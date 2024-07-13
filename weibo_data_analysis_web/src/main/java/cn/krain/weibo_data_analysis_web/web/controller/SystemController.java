package cn.krain.weibo_data_analysis_web.web.controller;

import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import cn.krain.weibo_data_analysis_web.result.ResultUtil;
import cn.krain.weibo_data_analysis_web.service.SystemUserService;
import cn.krain.weibo_data_analysis_web.util.MD5Util;
import cn.krain.weibo_data_analysis_web.vo.SystemUserVo;
import com.alibaba.fastjson.JSONObject;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 23:35
 * 用于系统用户登录、登出的请求控制
 */

/**
 * @ResponseBody注解既可以在方法上使用，也可以在类上使用，在类上使用表明该类中所有方法均返回JSON数据，
 * 也可以与@Controller注解合并为@RestController。
 * 它的作用是将controller的方法返回的对象通过适当的转换器转换为指定的格式之后，写入到response对象的body区，
 * 通常用来返回JSON数据或者是XML数据。
 */
@Api("系统用户登录登出相关接口")
@Controller
@ResponseBody
@RequestMapping("/user")
public class SystemController {

    @Autowired
    private SystemUserService systemUserService;

    @PostMapping("/login")
    @ApiOperation("根据用户名密码获取用户token接口")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "username", value = "用户名", dataType = "string"),
            @ApiImplicitParam(name = "password", value = "密码", dataType = "string")
    })
    public Object login_get_token(@RequestBody String json){
        JSONObject jsonObject = JSONObject.parseObject(json);
        String username = jsonObject.getString("username");
        String password = jsonObject.getString("password");
        Map<String, String> map = new HashMap<>();
        map.put("username", username);
        map.put("password", MD5Util.getMD5(password));
        try {
            SystemUser systemUser = systemUserService.userLogin(map);
            JSONObject resultData = new JSONObject();
            resultData.put("token", systemUser.getToken());
            return ResultUtil.success("登录成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("用户名或密码错误", false);
        }
    }

    @GetMapping("/info")
    @ApiOperation("通过用户token获取用户信息接口")
    @ApiImplicitParam(name = "token", value = "用户令牌", dataType = "string")
    public Object login_get_info(String token){
        try {
//            SystemUser systemUser = systemUserService.getUserByToken(token);
            SystemUserVo systemUserVo = systemUserService.getUserVoByToken(token);
            JSONObject resultData = new JSONObject();
            resultData.put("id", systemUserVo.getId());
            resultData.put("name", systemUserVo.getUsername());
            resultData.put("role_id", systemUserVo.getRole_id());
            resultData.put("token", systemUserVo.getToken());
            resultData.put("role", systemUserVo.getRole_name());
            resultData.put("avatar", systemUserVo.getAvatar());
            resultData.put("create_time", systemUserVo.getCreate_time());
            // 解析路由数组
            String[] routes = systemUserVo.getRole_menu().split("/");
            resultData.put("routes", routes);
            resultData.put("describe", systemUserVo.getRole_represent());
            return ResultUtil.success("登录成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("用户名或密码错误", false);
        }
    }

    @PostMapping("/logout")
    @ApiOperation("响应用户退出请求")
    public Object logout(){
        return ResultUtil.success("用户退出成功", true);
    }

}
