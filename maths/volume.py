"""
Find Volumes of Various Shapes.
Wikipedia reference: https://en.wikipedia.org/wiki/Volume
"""
from __future__ import annotations

from math import pi, pow


def vol_cube(side_length: int | float) -> float:
    """
    Calculate the Volume of a Cube.
    >>> vol_cube(1)
    1.0
    >>> vol_cube(3)
    27.0
    >>> vol_cube(-1)
    Traceback (most recent call last):
        ...
    ValueError: vol_cube() only accepts non-negative values
    """
    if side_length < 0:
        raise ValueError("vol_cube() only accepts non-negative values")
    return pow(side_length, 3)


def vol_spherical_cap(height: float, radius: float) -> float:
    """
    Calculate the Volume of the spherical cap.
    :return 1/3 pi * height ^ 2 * (3 * radius - height)
    >>> vol_spherical_cap(1, 2)
    5.235987755982988
    >>> vol_spherical_cap(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: vol_spherical_cap() only accepts non-negative values
    >>> vol_spherical_cap(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: vol_spherical_cap() only accepts non-negative values
    """
    if height < 0 or radius < 0:
        raise ValueError("vol_spherical_cap() only accepts non-negative values")
    return 1 / 3 * pi * pow(height, 2) * (3 * radius - height)


def vol_spheres_intersect(
    radius_1: float, radius_2: float, centers_distance: float
) -> float:
    """
    Calculate the volume of the intersection of two spheres.
    The intersection is composed by two spherical caps and therefore its volume is the
    sum of the volumes of the spherical caps. First, it calculates the heights (h1, h2)
    of the spherical caps, then the two volumes and it returns the sum.
    The height formulas are
    h1 = (radius_1 - radius_2 + centers_distance)
       * (radius_1 + radius_2 - centers_distance)
       / (2 * centers_distance)
    h2 = (radius_2 - radius_1 + centers_distance)
       * (radius_2 + radius_1 - centers_distance)
       / (2 * centers_distance)
    if centers_distance is 0 then it returns the volume of the smallers sphere
    :return vol_spherical_cap(h1, radius_2) + vol_spherical_cap(h2, radius_1)
    >>> vol_spheres_intersect(2, 2, 1)
    21.205750411731103
    >>> vol_spheres_intersect(-2, 2, 1)
    Traceback (most recent call last):
        ...
    ValueError: vol_spheres_intersect() only accepts non-negative values
    >>> vol_spheres_intersect(2, -2, 1)
    Traceback (most recent call last):
        ...
    ValueError: vol_spheres_intersect() only accepts non-negative values
    >>> vol_spheres_intersect(2, 2, -1)
    Traceback (most recent call last):
        ...
    ValueError: vol_spheres_intersect() only accepts non-negative values
    """
    if radius_1 < 0 or radius_2 < 0 or centers_distance < 0:
        raise ValueError("vol_spheres_intersect() only accepts non-negative values")
    if centers_distance == 0:
        return vol_sphere(min(radius_1, radius_2))

    h1 = (
        (radius_1 - radius_2 + centers_distance)
        * (radius_1 + radius_2 - centers_distance)
        / (2 * centers_distance)
    )
    h2 = (
        (radius_2 - radius_1 + centers_distance)
        * (radius_2 + radius_1 - centers_distance)
        / (2 * centers_distance)
    )

    return vol_spherical_cap(h1, radius_2) + vol_spherical_cap(h2, radius_1)


def vol_cuboid(width: float, height: float, length: float) -> float:
    """
    Calculate the Volume of a Cuboid.
    :return multiple of width, length and height
    >>> vol_cuboid(1, 1, 1)
    1.0
    >>> vol_cuboid(1, 2, 3)
    6.0
    >>> vol_cuboid(-1, 2, 3)
    Traceback (most recent call last):
        ...
    ValueError: vol_cuboid() only accepts non-negative values
    >>> vol_cuboid(1, -2, 3)
    Traceback (most recent call last):
        ...
    ValueError: vol_cuboid() only accepts non-negative values
    >>> vol_cuboid(1, 2, -3)
    Traceback (most recent call last):
        ...
    ValueError: vol_cuboid() only accepts non-negative values
    """
    if width < 0 or height < 0 or length < 0:
        raise ValueError("vol_cuboid() only accepts non-negative values")
    return float(width * height * length)


def vol_cone(area_of_base: float, height: float) -> float:
    """
    Calculate the Volume of a Cone.
    Wikipedia reference: https://en.wikipedia.org/wiki/Cone
    :return (1/3) * area_of_base * height
    >>> vol_cone(10, 3)
    10.0
    >>> vol_cone(1, 1)
    0.3333333333333333
    >>> vol_cone(-1, 1)
    Traceback (most recent call last):
        ...
    ValueError: vol_cone() only accepts non-negative values
    >>> vol_cone(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: vol_cone() only accepts non-negative values
    """
    if height < 0 or area_of_base < 0:
        raise ValueError("vol_cone() only accepts non-negative values")
    return area_of_base * height / 3.0


def vol_right_circ_cone(radius: float, height: float) -> float:
    """
    Calculate the Volume of a Right Circular Cone.
    Wikipedia reference: https://en.wikipedia.org/wiki/Cone
    :return (1/3) * pi * radius^2 * height
    >>> vol_right_circ_cone(2, 3)
    12.566370614359172
    >>> vol_right_circ_cone(-1, 1)
    Traceback (most recent call last):
        ...
    ValueError: vol_right_circ_cone() only accepts non-negative values
    >>> vol_right_circ_cone(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: vol_right_circ_cone() only accepts non-negative values
    """
    if height < 0 or radius < 0:
        raise ValueError("vol_right_circ_cone() only accepts non-negative values")
    return pi * pow(radius, 2) * height / 3.0


def vol_prism(area_of_base: float, height: float) -> float:
    """
    Calculate the Volume of a Prism.
    Wikipedia reference: https://en.wikipedia.org/wiki/Prism_(geometry)
    :return V = Bh
    >>> vol_prism(10, 2)
    20.0
    >>> vol_prism(11, 1)
    11.0
    >>> vol_prism(-1, 1)
    Traceback (most recent call last):
        ...
    ValueError: vol_prism() only accepts non-negative values
    >>> vol_prism(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: vol_prism() only accepts non-negative values
    """
    if height < 0 or area_of_base < 0:
        raise ValueError("vol_prism() only accepts non-negative values")
    return float(area_of_base * height)


def vol_pyramid(area_of_base: float, height: float) -> float:
    """
    Calculate the Volume of a Pyramid.
    Wikipedia reference: https://en.wikipedia.org/wiki/Pyramid_(geometry)
    :return  (1/3) * Bh
    >>> vol_pyramid(10, 3)
    10.0
    >>> vol_pyramid(1.5, 3)
    1.5
    >>> vol_pyramid(-1, 1)
    Traceback (most recent call last):
        ...
    ValueError: vol_pyramid() only accepts non-negative values
    >>> vol_pyramid(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: vol_pyramid() only accepts non-negative values
    """
    if height < 0 or area_of_base < 0:
        raise ValueError("vol_pyramid() only accepts non-negative values")
    return area_of_base * height / 3.0


def vol_sphere(radius: float) -> float:
    """
    Calculate the Volume of a Sphere.
    Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
    :return (4/3) * pi * r^3
    >>> vol_sphere(5)
    523.5987755982989
    >>> vol_sphere(1)
    4.1887902047863905
    >>> vol_sphere(-1)
    Traceback (most recent call last):
        ...
    ValueError: vol_sphere() only accepts non-negative values
    """
    if radius < 0:
        raise ValueError("vol_sphere() only accepts non-negative values")
    return 4 / 3 * pi * pow(radius, 3)


def vol_hemisphere(radius: float) -> float:
    """Calculate the volume of a hemisphere
    Wikipedia reference: https://en.wikipedia.org/wiki/Hemisphere
    Other references: https://www.cuemath.com/geometry/hemisphere
    :return 2/3 * pi * radius^3
    >>> vol_hemisphere(1)
    2.0943951023931953
    >>> vol_hemisphere(7)
    718.3775201208659
    >>> vol_hemisphere(-1)
    Traceback (most recent call last):
        ...
    ValueError: vol_hemisphere() only accepts non-negative values
    """
    if radius < 0:
        raise ValueError("vol_hemisphere() only accepts non-negative values")
    return 2 / 3 * pi * pow(radius, 3)


def vol_circular_cylinder(radius: float, height: float) -> float:
    """Calculate the Volume of a Circular Cylinder.
    Wikipedia reference: https://en.wikipedia.org/wiki/Cylinder
    :return pi * radius^2 * height
    >>> vol_circular_cylinder(1, 1)
    3.141592653589793
    >>> vol_circular_cylinder(4, 3)
    150.79644737231007
    >>> vol_circular_cylinder(-1, 1)
    Traceback (most recent call last):
        ...
    ValueError: vol_circular_cylinder() only accepts non-negative values
    >>> vol_circular_cylinder(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: vol_circular_cylinder() only accepts non-negative values
    """
    if height < 0 or radius < 0:
        raise ValueError("vol_circular_cylinder() only accepts non-negative values")
    return pi * pow(radius, 2) * height


def vol_hollow_circular_cylinder(
    inner_radius: float, outer_radius: float, height: float
) -> float:
    """Calculate the Volume of a Hollow Circular Cylinder.
    >>> vol_hollow_circular_cylinder(1, 2, 3)
    28.274333882308138
    >>> vol_hollow_circular_cylinder(-1, 2, 3)
    Traceback (most recent call last):
        ...
    ValueError: vol_hollow_circular_cylinder() only accepts non-negative values
    >>> vol_hollow_circular_cylinder(1, -2, 3)
    Traceback (most recent call last):
        ...
    ValueError: vol_hollow_circular_cylinder() only accepts non-negative values
    >>> vol_hollow_circular_cylinder(1, 2, -3)
    Traceback (most recent call last):
        ...
    ValueError: vol_hollow_circular_cylinder() only accepts non-negative values
    >>> vol_hollow_circular_cylinder(2, 1, 3)
    Traceback (most recent call last):
        ...
    ValueError: outer_radius must be greater than inner_radius
    """
    if inner_radius < 0 or outer_radius < 0 or height < 0:
        raise ValueError(
            "vol_hollow_circular_cylinder() only accepts non-negative values"
        )
    if outer_radius <= inner_radius:
        raise ValueError("outer_radius must be greater than inner_radius")
    return pi * (pow(outer_radius, 2) - pow(inner_radius, 2)) * height


def vol_conical_frustum(height: float, radius_1: float, radius_2: float) -> float:
    """Calculate the Volume of a Conical Frustum.
    Wikipedia reference: https://en.wikipedia.org/wiki/Frustum
    :return 1/3 * pi * height * (radius_1^2 + radius_top^2 + radius_1 * radius_2)
    >>> vol_conical_frustum(45, 7, 28)
    48490.482608158454
    >>> vol_conical_frustum(1, 1, 2)
    7.330382858376184
    >>> vol_conical_frustum(-2, 2, 1)
    Traceback (most recent call last):
        ...
    ValueError: vol_conical_frustum() only accepts non-negative values
    >>> vol_conical_frustum(2, -2, 1)
    Traceback (most recent call last):
        ...
    ValueError: vol_conical_frustum() only accepts non-negative values
    >>> vol_conical_frustum(2, 2, -1)
    Traceback (most recent call last):
        ...
    ValueError: vol_conical_frustum() only accepts non-negative values
    """
    if radius_1 < 0 or radius_2 < 0 or height < 0:
        raise ValueError("vol_conical_frustum() only accepts non-negative values")
    return (
        1
        / 3
        * pi
        * height
        * (pow(radius_1, 2) + pow(radius_2, 2) + radius_1 * radius_2)
    )


def main():
    """Print the Results of Various Volume Calculations."""
    print("Volumes:")
    print("Cube: " + str(vol_cube(2)))  # = 8
    print("Cuboid: " + str(vol_cuboid(2, 2, 2)))  # = 8
    print("Cone: " + str(vol_cone(2, 2)))  # ~= 1.33
    print("Right Circular Cone: " + str(vol_right_circ_cone(2, 2)))  # ~= 8.38
    print("Prism: " + str(vol_prism(2, 2)))  # = 4
    print("Pyramid: " + str(vol_pyramid(2, 2)))  # ~= 1.33
    print("Sphere: " + str(vol_sphere(2)))  # ~= 33.5
    print("Hemisphere: " + str(vol_hemisphere(2)))  # ~= 16.75
    print("Circular Cylinder: " + str(vol_circular_cylinder(2, 2)))  # ~= 25.1
    print(
        "Hollow Circular Cylinder: " + str(vol_hollow_circular_cylinder(1, 2, 3))
    )  # ~= 28.3
    print("Conical Frustum: " + str(vol_conical_frustum(2, 2, 4)))  # ~= 58.6
    print("Spherical cap: " + str(vol_spherical_cap(1, 2)))  # ~= 5.24
    print("Spheres intersetion: " + str(vol_spheres_intersect(2, 2, 1)))  # ~= 21.21


if __name__ == "__main__":
    main()
