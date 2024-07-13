package cn.krain.weibo_data_analysis_web.web.controller;

import cn.krain.weibo_data_analysis_web.service.SystemUserService;

import org.python.core.Py;
import org.python.util.PythonInterpreter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.Date;

/**
 * @author cc
 * @data 2022/5/5 - 23:35
 */
/**
 * @ResponseBody注解既可以在方法上使用，也可以在类上使用，在类上使用表明该类中所有方法均返回JSON数据，
 * 也可以与@Controller注解合并为@RestController。
 * 它的作用是将controller的方法返回的对象通过适当的转换器转换为指定的格式之后，写入到response对象的body区，
 * 通常用来返回JSON数据或者是XML数据。
 */
@Controller
@ResponseBody
@Component
public class SystemTimingController {

    /**
     * 设置每四个小时获取一次数据
     */
    @Scheduled(initialDelay = 1000, fixedDelay = 14400000)
    public void getData(){
        System.out.println("获取数据完成：" + new Date());
        PythonInterpreter interpreter = new PythonInterpreter();
        // 调用指定路径下的Python文件
//        interpreter.execfile("D:\\Program\\Pycharm\\weibo_data\\weibo_data\\spiders\\StartScrapy.py");
    }
    /**
     * 设置每四个小时分析一次数据
     */
    @Scheduled(initialDelay = 18000000, fixedDelay = 14400000)
    public void anaylsisData() {
        System.out.println("分析数据完成：" + new Date());
        PythonInterpreter interpreter = new PythonInterpreter();
        // 调用指定路径下的Python文件
//        interpreter.execfile("D:\\Program\\Pycharm\\weibo_data\\weibo_data\\analysis\\worldcloud.py");
//        interpreter.execfile("D:\\Program\\Pycharm\\weibo_data\\weibo_data\\analysis\\hot_topic.py");
//        interpreter.execfile("D:\\Program\\Pycharm\\weibo_data\\weibo_data\\analysis\\emotion_analysis.py");
//        interpreter.execfile("D:\\Program\\Pycharm\\weibo_data\\weibo_data\\analysis\\time_filter.py");
//        interpreter.execfile("D:\\Program\\Pycharm\\weibo_data\\weibo_data\\analysis\\comment_map.py");
//        interpreter.execfile("D:\\Program\\Pycharm\\weibo_data\\weibo_data\\analysis\\comment_emotion.py");
    }

    /**
     * 设置每二四个小时清理一次过期数据
     */
    @Scheduled(initialDelay = 1000, fixedDelay = 86400000)
    public void timingTest() {
        System.out.println("清理过期数据完成：" + new Date());
        PythonInterpreter interpreter = new PythonInterpreter();
        // 调用指定路径下的Python文件
//        interpreter.execfile("D:\\Program\\Pycharm\\weibo_data\\weibo_data\\spiders\\StartScrapy.py");
    }
}
