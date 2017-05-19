
import scala.concurrent.duration._

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._

class RecordedSimulation extends Simulation {

	val httpProtocol = http
		.baseURL("http://localhost:8080")
		.inferHtmlResources()
		.acceptHeader("application/json, text/javascript, */*; q=0.01")
		.acceptEncodingHeader("gzip, deflate, sdch")
		.acceptLanguageHeader("en-GB,en-US;q=0.8,en;q=0.6")
		.userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

	val headers_0 = Map(
		"Accept" -> "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Upgrade-Insecure-Requests" -> "1")

	val headers_1 = Map(
		"Accept" -> "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding" -> "gzip, deflate, br",
		"Origin" -> "http://localhost:8080",
		"Upgrade-Insecure-Requests" -> "1")

	val headers_2 = Map("X-Requested-With" -> "XMLHttpRequest")

	val headers_4 = Map(
		"Accept" -> "text/html, */*; q=0.01",
		"X-Requested-With" -> "XMLHttpRequest")

	val headers_13 = Map("Accept" -> "image/webp,image/*,*/*;q=0.8")

    val uri1 = "http://localhost:8080/WebGoat"

	val scn = scenario("RecordedSimulation")
		.exec(http("request_0")
			.get("/WebGoat/login.mvc")
			.headers(headers_0))
		.pause(8)
		.exec(http("request_1")
			.post("/WebGoat/j_spring_security_check")
			.headers(headers_1)
			.formParam("username", "webgoat")
			.formParam("password", "webgoat")
			.resources(http("request_2")
			.get("/WebGoat/service/lessonmenu.mvc")
			.headers(headers_2),
            http("request_3")
			.get("/WebGoat/service/debug/labels.mvc")
			.headers(headers_2),
            http("request_4")
			.get("/WebGoat/attack?Screen=360466308&menu=5")
			.headers(headers_4),
            http("request_5")
			.get("/WebGoat/service/lessonmenu.mvc")
			.headers(headers_2),
            http("request_6")
			.get("/WebGoat/attack?Screen=360466308&menu=5")
			.headers(headers_4),
            http("request_7")
			.get("/WebGoat/service/lessonmenu.mvc")
			.headers(headers_2),
            http("request_8")
			.get("/WebGoat/service/lessoninfo.mvc")
			.headers(headers_2),
            http("request_9")
			.get("/WebGoat/service/lessonplan.mvc")
			.headers(headers_4),
            http("request_10")
			.get("/WebGoat/service/solution.mvc")
			.headers(headers_4),
            http("request_11")
			.get("/WebGoat/service/hint.mvc")
			.headers(headers_2),
            http("request_12")
			.get("/WebGoat/service/lessonprogress.mvc")
			.headers(headers_2),
            http("request_13")
			.get("/WebGoat/plugin_extracted/plugin/HowToWork/lessonPlans/en/HowToWork_files/interface.png")
			.headers(headers_13),
            http("request_14")
			.get("/WebGoat/service/cookie.mvc")
			.headers(headers_2),
            http("request_15")
			.get("/WebGoat/service/source.mvc")
			.headers(headers_4),
            http("request_16")
			.get("/WebGoat/service/lessonmenu.mvc")
			.headers(headers_2),
            http("request_17")
			.get("/WebGoat/service/lessoninfo.mvc")
			.headers(headers_2),
            http("request_18")
			.get("/WebGoat/service/lessonplan.mvc")
			.headers(headers_4),
            http("request_19")
			.get("/WebGoat/service/source.mvc")
			.headers(headers_4),
            http("request_20")
			.get("/WebGoat/service/hint.mvc")
			.headers(headers_2),
            http("request_21")
			.get("/WebGoat/service/cookie.mvc")
			.headers(headers_2),
            http("request_22")
			.get("/WebGoat/service/lessonprogress.mvc")
			.headers(headers_2),
            http("request_23")
			.get("/WebGoat/service/lessonmenu.mvc")
			.headers(headers_2),
            http("request_24")
			.get("/WebGoat/service/solution.mvc")
			.headers(headers_4)))
		.pause(2)
		.exec(http("request_25")
			.get("/WebGoat/service/lessonmenu.mvc")
			.headers(headers_2)
			.resources(http("request_26")
			.get("/WebGoat/attack?Screen=1778575388&menu=500")
			.headers(headers_4),
            http("request_27")
			.get("/WebGoat/service/lessoninfo.mvc")
			.headers(headers_2),
            http("request_28")
			.get("/WebGoat/service/lessonplan.mvc")
			.headers(headers_4),
            http("request_29")
			.get("/WebGoat/service/cookie.mvc")
			.headers(headers_2),
            http("request_30")
			.get("/WebGoat/service/hint.mvc")
			.headers(headers_2),
            http("request_31")
			.get("/WebGoat/service/source.mvc")
			.headers(headers_4),
            http("request_32")
			.get("/WebGoat/service/solution.mvc")
			.headers(headers_4),
            http("request_33")
			.get("/WebGoat/service/lessonprogress.mvc")
			.headers(headers_2),
            http("request_34")
			.get("/WebGoat/service/lessonmenu.mvc")
			.headers(headers_2)))
		.pause(4)
		.exec(http("request_35")
			.get("/WebGoat/service/lessonmenu.mvc")
			.headers(headers_2)
			.resources(http("request_36")
			.get("/WebGoat/attack?Screen=736032128&menu=600")
			.headers(headers_4),
            http("request_37")
			.get("/WebGoat/service/lessoninfo.mvc")
			.headers(headers_2),
            http("request_38")
			.get("/WebGoat/service/solution.mvc")
			.headers(headers_4),
            http("request_39")
			.get("/WebGoat/service/lessonprogress.mvc")
			.headers(headers_2),
            http("request_40")
			.get("/WebGoat/service/source.mvc")
			.headers(headers_4),
            http("request_41")
			.get("/WebGoat/service/cookie.mvc")
			.headers(headers_2),
            http("request_42")
			.get("/WebGoat/service/hint.mvc")
			.headers(headers_2),
            http("request_43")
			.get("/WebGoat/service/lessonmenu.mvc")
			.headers(headers_2),
            http("request_44")
			.get("/WebGoat/service/lessonplan.mvc")
			.headers(headers_4)))
		.pause(5)
		.exec(http("request_45")
			.get("/WebGoat/j_spring_security_logout")
			.headers(headers_0))

	setUp(scn.inject(atOnceUsers(10))).protocols(httpProtocol).assertions(global.responseTime.mean.lt(2000))
}
