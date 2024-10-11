const express = require("express");
const morgan = require("morgan");
const cookieParser = require("cookie-parser");
const cors = require("cors");

const dotenv = require("dotenv");
dotenv.config({ path: "./.env" });

const crewaiRoute = require("./features/crewai/crewaiApis");

const port = process.env.PORT || 5500;

// USE MODULES HERE
const app = express();

app.use(morgan("dev"));

// const allowedOrigins = [
//   'http://localhost:4200',
//   'http://192.1.200.38:4200'
// ];
// app.use(cors({
//   origin: function (origin, callback) {
//     if (!origin || allowedOrigins.indexOf(origin) !== -1) {
//       callback(null, true);
//     } else {
//       callback(new Error('Not allowed by CORS'));
//     }
//   },
//   credentials: true,
// }));

app.use(express.json());
app.use(cookieParser());

// USE ROUTES HERE
app.use("/api/v1/crewai", crewaiRoute);

app.listen(port, () => {
  console.log(`server is listening on ${port}`);
});
