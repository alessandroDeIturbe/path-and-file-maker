#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <experimental/filesystem>
#include <fstream>
#include <cstdlib>

using namespace std;
namespace fs = std::experimental::filesystem;

string error(string message)
{
    return "\033[41m\033[97m" + message + "\033[0m";
}

string message(string message)
{
    return "\033[44m\033[97m" + message + "\033[0m";
}

bool detect_file(string file)
{
    return file.find(".") != string::npos;
}

bool detect_multiple_files(string files)
{
    return files.find(',') != string::npos;
}

int main(int argc, char const *argv[])
{

    vector<string> argvs;

    for (int i = 0; i < argc; i++)
    {
        argvs.push_back(argv[i]);
    }

    argvs.erase(argvs.begin());

    int argvc = argvs.size();

    if (!(0 < argvc && argvc < 3))
    {
        if (argvc == 0)
        {
            cout << error("ERROR: No arguments given.") << endl;
        }
        else
        {
            cout << error("ERROR: Too many arguments given.") << endl;
        }

        cout << error("Usage: pfm <path> <start-directory(OPTIONAL)>") << endl;
        cout << error("Use \"pfm --help\" for more information.") << endl;
    }
    else
    {
        if (argvs[0] == "-h" || argvs[0] == "--help")
        {
            cout << message("USAGE: pfm [path] [start-folder (if you want to start from a specific folder)]") << endl;
            cout << message("Example: pfm folder,file.ext/folder/file.ext [OPTIONAL] starting_folder/") << endl;
            std::exit(0);
        }
        else
        {
            if (argvc == 2)
            {
                string start_folder = argvs[1];
                if (!fs::exists(start_folder))
                {
                    cout << error("ERROR: start folder does not exists.");
                    std::string answer;
                    std::cout << "Continue in the current folder? y/[N]: ";
                std:
                    getline(std::cin, answer);
                    if (answer != "y")
                    {
                        std::exit(1);
                    }
                    else
                    {
                        fs::current_path(start_folder);
                    }
                }
            }

            // !
            // ! To fix from here
            // !

            std::string path = argvs[0];
            std::stringstream ss(path);
            std::string token;
            std::vector<std::string> path_tokens;

            while (std::getline(ss, token, '/'))
            {
                path_tokens.push_back(token);
            }

            for (int i; i < path_tokens.size(), ++i;)
            {
                cout << path_tokens[i] << endl;
            }
        }
    }

    return 0;
}
