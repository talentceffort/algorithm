//파라미터 some_list를 거꾸로 뒤집는 함수
function flip(some_list) {
    // 코드를 입력하세요.
    if(some_list.length === 1) {
        return some_list;
    } else {
        let temp = some_list.slice(-1);
        console.log(temp.concat(flip(some_list.slice(0, some_list.length - 1))))
        return temp.concat(flip(some_list.slice(0, some_list.length - 1)));
    }
}


// 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
console.log(some_list)