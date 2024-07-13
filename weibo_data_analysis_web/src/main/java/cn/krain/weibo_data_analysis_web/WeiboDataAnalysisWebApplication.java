package cn.krain.weibo_data_analysis_web;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.Banner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
@ComponentScan(basePackages = {"cn.krain"})
@MapperScan("cn.krain.weibo_data_analysis_web.dao")
public class WeiboDataAnalysisWebApplication {
     public static void main(String[] args) {
         SpringApplication.run(WeiboDataAnalysisWebApplication.class, args);
     }
    /*public static void main(String[] args) {
        SpringApplication springApplication = new SpringApplication(WeiboDataAnalysisWebApplication.class);
        // 关闭启动logo
        // springApplication.setBannerMode(Banner.Mode.OFF);
        springApplication.run(args);
    }*/
}
