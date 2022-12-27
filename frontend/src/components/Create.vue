<template>
  <div class="container mt-4">
    <form @submit="insertArticle">
      <h5 class="text-style">申请签证目标国家:</h5>
      <input
        type="text"
        class="form-control"
        placeholder="Please enter"
        v-model="country"
      />
      <br />

      <p5 class="text-style">订单种类：机票/机票+酒店/机票+酒店+保险单:</p5>
      <el-select v-model="order_type" placeholder="请选择" width="260">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <input type="text" class="form-control" placeholder="Please enter" />
      <br />

      <h5 class="text-style">出发日期:</h5>
      <el-date-picker
        v-model="dp_date"
        type="date"
        placeholder="Pick a date"
        :default-value="new Date(2022, 1, 1)"
      />
      <input type="text" class="form-control" placeholder="Please enter " />
      <h5 class="text-style">返回日期:</h5>
      <el-date-picker
        v-model="arr_date"
        type="date"
        placeholder="Pick a date"
        :default-value="new Date(2022, 1, 1)"
      />
      <input type="text" class="form-control" placeholder="Please enter " />
      <br />
      <h5 class="text-style">
        此处输入客人数目，名单列表（中英文都需要）和特别备注（如果有）：
      </h5>
      <textarea
        rows="6"
        class="form-control"
        placeholder="Please enter ，请参考如下格式：
              客人1 姓：ZHANG 名： MING WEI
              客人2 姓：LI 名：AI GUO"
        v-model="body"
      >
      </textarea>

      <button class="btn btn-success mt-4">提交订单</button>
      <button class="btn btn-danger mt-4" @click="returnhome">返回</button>
    </form>
    <div
      v-if="error"
      class="alert alert-warning alert-dismissible fade shwo mt-5"
      role="alert"
    >
      <strong>{{ error }}</strong>
    </div>
  </div>
</template>

<script>
const shortcuts = [
  {
    text: "Last week",
    value: () => {
      const end = new Date();
      const start = new Date();
      start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
      return [start, end];
    },
  },
  {
    text: "Last month",
    value: () => {
      const end = new Date();
      const start = new Date();
      start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
      return [start, end];
    },
  },
  {
    text: "Last 3 months",
    value: () => {
      const end = new Date();
      const start = new Date();
      start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
      return [start, end];
    },
  },
];

export default {
  components: {},

  data() {
    return {
      country: null,
      order_type: null,
      dp_date: null,
      arr_date: null,
      value: "",
      v3parr_date: "",
      v3pdp_date: "",
      options: [
        {
          value: "机票单（单项服务）",
          label: "机票单（单项服务）",
        },
        {
          value: "酒店单（单项服务）",
          label: "酒店单（单项服务）",
        },

        {
          value: "机票单+酒店单",
          label: "机票单+酒店单",
        },
        {
          value: "机票单+酒店单+申根专项保险单",
          label: "机票单+酒店单+申根专项保险单",
        },
      ],
      body: null,
      error: null,
    };
  },
  created() {
    // 初始化下拉框
  },

  methods: {
    returnhome() {
      this.$router.push({
        name: "home",
      });
    },

    onChange(name, value, index) {
      // eslint-disable-next-line no-mixed-spaces-and-tabs
      console.log("item:", name, value, index);
      // eslint-disable-next-line no-mixed-spaces-and-tabs
    },

    insertArticle() {
      if (
        !this.body ||
        !this.dp_date ||
        !this.order_type ||
        !this.country ||
        !this.arr_date
      ) {
        this.error = "请填写所有必填内容";
      } else {
        fetch("http://localhost:5000/add", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            country: this.country,
            order_type: this.order_type,
            dp_date: this.dp_date,
            arr_date: this.arr_date,
            body: this.body,
          }),
        })
          .then((resp) => resp.json())
          .then(() => {
            this.$router.push({
              name: "home",
            });
          })
          .catch((error) => {
            console.log(error);
          });
      }
      this.$router.push({
        name: "home",
      });
    },
  },
};
</script>

<style scoped>
.text-style {
  font-size: 20px !important;
  display: flex;
  font-weight: 400;
  font-family: "Fira Sans", sans-serif;
  color: rgb(42, 108, 206) !important;
}
.demo-date-picker {
  display: flex;
  width: 100%;
  padding: 0;
  flex-wrap: wrap;
}
.demo-date-picker .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  flex: 1;
}
.demo-date-picker .block:last-child {
  border-right: none;
}
.demo-date-picker .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}
</style>
