import axios from 'axios'
import dotenv from 'dotenv'
dotenv.config()
async function a(){
    axios.request(
        Object.assign({
            method:"GET",
            headers:{
                Cookie:process.env.COOKIE as string
            }
        },{
            url:'https://leetcode.com/api/problems/all/'
        })
    )
    .then(res => {
        const questions = res.data.stat_status_pairs;
        const promises = [];
        console.log(questions)
        console.log(res)
    })
}a()