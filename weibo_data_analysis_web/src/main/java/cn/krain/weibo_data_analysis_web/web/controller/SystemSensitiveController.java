package cn.krain.weibo_data_analysis_web.web.controller;

import cn.krain.weibo_data_analysis_web.entity.SystemSensitiveWord;
import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import cn.krain.weibo_data_analysis_web.entity.SystemWeekRank;
import cn.krain.weibo_data_analysis_web.result.ResultUtil;
import cn.krain.weibo_data_analysis_web.service.SystemSensitiveWordService;
import cn.krain.weibo_data_analysis_web.service.SystemUserService;
import cn.krain.weibo_data_analysis_web.service.SystemWeekRankService;
import cn.krain.weibo_data_analysis_web.util.DataTimeUtil;
import cn.krain.weibo_data_analysis_web.util.MD5Util;
import cn.krain.weibo_data_analysis_web.util.UUIDUtil;
import com.alibaba.fastjson.JSONObject;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

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
@RequestMapping("/sensitive")
public class SystemSensitiveController {

    @Autowired
    private SystemSensitiveWordService sensitiveWordService;

    @Autowired
    private SystemWeekRankService weekRankService;

    @GetMapping("/queryWord")
    @ApiOperation("查询敏感词")
    public Object queryWord(){
        try {
            List<SystemSensitiveWord> sensitiveWordList = sensitiveWordService.getAllSenWord();
            JSONObject resultData = new JSONObject();
            resultData.put("sensitiveWordList", sensitiveWordList);
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
        sensitiveWordService.delSenWordById(id);
        return ResultUtil.success("敏感词删除成功", true);
    }


    /**
     * 处理新增用户请求
     * @param json
     * @return
     */
    @PostMapping("/add")
    @ApiOperation("根据参数id，新增一个敏感词")
    public Object addUser(@RequestBody String json){
        JSONObject jsonObject = JSONObject.parseObject(json);
        String sensitive_word = jsonObject.getString("sensitive_word");
        String creater = jsonObject.getString("creater");
        SystemSensitiveWord sensitiveWord  = new SystemSensitiveWord();
        sensitiveWord.setId(UUIDUtil.getUUID());
        sensitiveWord.setSensitive_word(sensitive_word);
        // 获取当前时间
        sensitiveWord.setCreate_time(DataTimeUtil.getSysTime());
        sensitiveWord.setCreater(creater);
        sensitiveWordService.addSenWord(sensitiveWord);
        return ResultUtil.success("用户添加成功", true);
    }

    @GetMapping("/queryTopicByWord")
    @ApiOperation("根据敏感词查询话题")
    public Object queryTopicByWord(String senWord){
        try {
            List<SystemWeekRank> weekRankList = weekRankService.getTopicByWord(senWord);
            JSONObject resultData = new JSONObject();
            resultData.put("weekRankList", weekRankList);
            return ResultUtil.success("查询成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询错误", false);
        }
    }

    @GetMapping("/queryNumByWord")
    @ApiOperation("根据敏感词查询数量")
    public Object queryNumByWord(String title){
        try {
            List<SystemWeekRank> weekRankList = weekRankService.getNumByWord(title);
            JSONObject resultData = new JSONObject();
            resultData.put("weekRankList", weekRankList);
            return ResultUtil.success("查询成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询错误", false);
        }
    }

}
