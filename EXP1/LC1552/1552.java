class Solution {
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);
        int low=1;
        int high = position[position.length - 1] - position[0];
        int ans=0 ;
        while(low<=high){
            int mid = low + (high - low )/2;
            if(possible(position,m,mid)){
                ans=mid;
                low=mid+1;
            }
            else{
                high = mid - 1;
            }
        }
        return ans ;
    }
    boolean possible(int[] pos , int m , int dist){
        int balls = 1;
        int last = pos[0];
        for(int i =1;i<pos.length;i++){
            if(pos[i] - last >= dist){
                balls++;
                last=pos[i];
            }
            if(balls == m){
                return true;
            }
        }
        return false;
    }
}