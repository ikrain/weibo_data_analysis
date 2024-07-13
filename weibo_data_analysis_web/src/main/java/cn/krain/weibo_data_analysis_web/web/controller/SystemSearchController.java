package cn.krain.weibo_data_analysis_web.web.controller;

import cn.krain.weibo_data_analysis_web.entity.SystemWeekRank;
import cn.krain.weibo_data_analysis_web.result.ResultUtil;
import cn.krain.weibo_data_analysis_web.service.SystemSearchTopicService;
import cn.krain.weibo_data_analysis_web.service.SystemWeekRankService;
import cn.krain.weibo_data_analysis_web.vo.SystemSearchTopicVo;
import cn.krain.weibo_data_analysis_web.vo.SystemWeekRankVo;
import com.alibaba.fastjson.JSONObject;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/10 - 18:35
 */
@Api("系统舆情检索模块接口")
@Controller
@ResponseBody
@RequestMapping("/search")
public class SystemSearchController {
    @Autowired
    private SystemSearchTopicService systemSearchTopicService;

    @GetMapping("/querySearchTopic")
    @ApiOperation("查询话题文章数据")
    public Object querySearchTopic(String page, String limit, String content){
        try {
            Map<String, Object> map = new HashMap<>();
            //更具page和limit来计算跳跃的数字  (limit 0,3)
            int pageInt = Integer.valueOf(page);
            int limitInt = Integer.valueOf(limit);
            int skipCount = (pageInt - 1) * limitInt;
            map.put("skipCount", skipCount);
            map.put("limit", limitInt);
            map.put("content", content);
            List<SystemSearchTopicVo> searchTopicVoList = systemSearchTopicService.querySearchTopic(map);
            int total = systemSearchTopicService.getTotalByContent(map);
            JSONObject resultData = new JSONObject();
            resultData.put("searchTopicVoList", searchTopicVoList);
            resultData.put("total", total);
            return ResultUtil.success("查询话题文章数据成功", resultData, true);
        }catch (Exception e){
            e.printStackTrace();
            // 登录失败返回提示信息
            return ResultUtil.error("查询话题文章数据失败", false);
        }
    }

}
