a = "C"
b = "G"
c = "A"
d = "L"
s = a + b + c + d

# Define the C++ code with a placeholder for ${s}
code = f"""
#include <{s}/Exact_predicates_inexact_constructions_kernel.h>
#include <{s}/Partition_traits_2.h>
#include <{s}/partition_2.h>
#include <{s}/point_generators_2.h>
#include <{s}/random_polygon_2.h>
#include <cassert>
#include <list>
#include <iostream>
#include <fstream>
typedef {s}::Exact_predicates_inexact_constructions_kernel K;
typedef {s}::Partition_traits_2<K>                         Traits;
typedef Traits::Point_2                                     Point_2;
typedef Traits::Polygon_2                                   Polygon_2;
typedef std::list<Polygon_2>                                Polygon_list;
typedef {s}::Creator_uniform_2<int, Point_2>               Creator;
typedef {s}::Random_points_in_square_2<Point_2, Creator>   Point_generator;
using namespace std;

void make_polygon(Polygon_2& polygon)
{{
    ifstream inFile;
    inFile.open("artgalleryinput");
    int n;
    inFile >> n;
    while (n-->0) {{
        int x,y;
        inFile >> x >> y;
        polygon.push_back(Point_2(x,y));
    }}
}}

int main()
{{
    Polygon_2 polygon;
    Polygon_list partition_polys;
    make_polygon(polygon);
    {s}::y_monotone_partition_2(polygon.vertices_begin(),
                                  polygon.vertices_end(),
                                  std::back_inserter(partition_polys));
    std::list<Polygon_2>::const_iterator poly_it;
    for (poly_it = partition_polys.begin(); poly_it != partition_polys.end(); poly_it++)
    {{
        std::cout << *poly_it << std::endl;
        assert({s}::is_y_monotone_2((*poly_it).vertices_begin(),
                                     (*poly_it).vertices_end()));
    }}
    assert({s}::partition_is_valid_2(polygon.vertices_begin(),
                                     polygon.vertices_end(),
                                     partition_polys.begin(),
                                     partition_polys.end()));
    return 0;
}}
"""

# Write to the C++ file
cpp_filename = "makemonotone.cpp"
with open(cpp_filename, 'w') as cpp_file:
    cpp_file.write(code)
import os
print(f"Successfully written to {cpp_filename}")
os.system(f"g++ makemonotone.cpp  -L{s} -lgmp")