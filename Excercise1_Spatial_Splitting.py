def split_region(x, y, width, height, min_size):
    if width < min_size or height < min_size:
        return

    half_w = width // 2
    half_h = height // 2

    split_region(x, y, half_w, half_h, min_size)
    split_region(x + half_w, y, half_w, half_h, min_size)
    split_region(x, y + half_h, half_w, half_h, min_size)
    split_region(x + half_w, y + half_h, half_w, half_h, min_size)


def count_points_in_region(points, region):
    count = 0

    for point in points:
        px, py = point

        if (px >= region[0] and
            px <  region[0] + region[2] and
            py >= region[1] and
            py <  region[1] + region[3]):
            count = count + 1

    return count


def find_dense_regions(points, x, y, width, height, min_size, density_threshold, result):
    region = (x, y, width, height)

    count = count_points_in_region(points, region)
    area = width * height
    density = count / area

    if density > density_threshold:
        result.append(region)

    if width < min_size or height < min_size:
        return

    half_w = width // 2
    half_h = height // 2

    
    find_dense_regions(points, x, y, half_w, half_h, min_size, density_threshold, result)
    find_dense_regions(points, x + half_w, y, half_w, half_h, min_size, density_threshold, result)
    find_dense_regions(points, x, y + half_h, half_w, half_h, min_size, density_threshold, result)
    find_dense_regions(points, x + half_w, y + half_h, half_w, half_h, min_size, density_threshold, result)



import random


points = [(random.randint(0, 99), random.randint(0, 99)) for i in range(100)]

result = []

find_dense_regions(
    points,
    x=0,
    y=0,
    width=100,
    height=100,
    min_size=10,
    density_threshold=0.01,
    result=result
)

print("Dense regions:", result)
print("Total:", len(result))