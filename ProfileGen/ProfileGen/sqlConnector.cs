using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace ProfileGen
{
    class sqlConnector
    {
        private MySqlConnection connection;
        private string server;
        private string database;
        private string uid;
        private string password;

        //constructor
        public sqlConnector()
        {
            server = "localhost";
            database = "profile_gen";

        }

    }
}
