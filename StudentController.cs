using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using p_28_EF.Models;

namespace p_28_EF.Controllers
{
    public class StudentController : Controller
    {
        // GET: Student
        public ActionResult Create()
        {
            return View();
        }



        [HttpPost]
        public ActionResult Create(Student s)
        {
            if (ModelState.IsValid)
            {
                ViewBag.Message = "Student Data Submitted Successfully!";
                return View("Success");
            }

            return View(s);
        }



    }
}