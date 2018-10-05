const apiTasksMock = {
  tasks: [
    {
      title: "Rasen mähen",
      duedate: "2018-10-05T11:23:02.587Z",
      status: 0,
      description: "",
      estimated_time_in_minutes: 30,
      user: 2
    },
    {
      title: "Einkäufe erledigen",
      duedate: "2018-10-05T11:23:02.587Z",
      status: 0,
      description: "",
      estimated_time_in_minutes: 40,
      user: 2
    },
    {
      title: "Die Wohnung wischen",
      duedate: "2018-10-05T11:23:02.587Z",
      status: 0,
      description: "",
      estimated_time_in_minutes: 50,
      user: 3
    },
  ],
};

const stati = {
  0: 'open',
  1: 'hidden',
  2: 'assigned',
  3: 'completed'
}

export default apiTasksMock;